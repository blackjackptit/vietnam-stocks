#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Load all Vietnamese stocks into the database
Fetches complete stock list from vnstock and populates database
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from vnstock import Listing
from config import get_database_connection
import time

def get_all_stocks():
    """Fetch all stocks from vnstock"""
    print("Fetching complete stock list from vnstock...")

    try:
        listing = Listing()
        all_stocks = []

        exchanges = ['HOSE', 'HNX', 'UPCOM']

        for exchange in exchanges:
            print(f"   Fetching {exchange} stocks...")
            try:
                df = listing.symbols_by_exchange(exchange=exchange)
                if df is not None and len(df) > 0:
                    stocks = df.to_dict('records')
                    all_stocks.extend(stocks)
                    print(f"   Found {len(stocks)} stocks on {exchange}")
                time.sleep(1)  # Rate limiting
            except Exception as e:
                print(f"   Warning: Error fetching {exchange}: {e}")
                continue

        print(f"\nTotal stocks found: {len(all_stocks)}")
        return all_stocks

    except Exception as e:
        print(f"Error fetching stock list: {e}")
        return []


def categorize_stock(symbol, name, sector, industry):
    """Determine stock category based on sector and industry"""
    symbol_upper = symbol.upper()
    name_lower = name.lower() if name else ''
    sector_lower = sector.lower() if sector else ''
    industry_lower = industry.lower() if industry else ''

    # Blue chips (VN30 components and large cap)
    vn30_symbols = [
        'VCB', 'BID', 'CTG', 'TCB', 'MBB', 'VPB', 'ACB', 'STB',
        'VNM', 'VIC', 'VHM', 'VRE', 'HPG', 'MSN', 'MWG', 'GAS',
        'FPT', 'PLX', 'SAB', 'POW', 'GVR', 'SSI', 'VJC', 'HDB',
        'PDR', 'TPB', 'BCM', 'DHG', 'KDH', 'NVL'
    ]
    if symbol_upper in vn30_symbols:
        return 'blue_chips'

    # Banks
    if 'bank' in sector_lower or 'bank' in industry_lower or 'bank' in name_lower:
        return 'banks'

    # Technology
    if any(x in sector_lower or x in industry_lower for x in ['technology', 'software', 'it', 'telecom']):
        return 'tech'

    # Real Estate
    if any(x in sector_lower or x in industry_lower for x in ['real estate', 'property', 'construction']):
        return 'real_estate'

    # Energy
    if any(x in sector_lower or x in industry_lower for x in ['energy', 'oil', 'gas', 'petro']):
        return 'oil_gas'

    # Consumer
    if any(x in sector_lower or x in industry_lower for x in ['consumer', 'retail', 'food', 'beverage']):
        return 'consumer'

    # Securities
    if 'securities' in sector_lower or 'securities' in industry_lower:
        return 'securities'

    # Manufacturing
    if 'manufacturing' in sector_lower or 'industrial' in sector_lower:
        return 'manufacturing'

    # Materials
    if 'materials' in sector_lower or 'steel' in industry_lower:
        return 'materials'

    # Healthcare
    if any(x in sector_lower or x in industry_lower for x in ['health', 'pharma', 'medical']):
        return 'healthcare'

    # Default
    return 'other'


def populate_database(stocks_data):
    """Populate database with all stocks"""
    print("\n Populating database...")

    try:
        conn = get_database_connection()
        cursor = conn.cursor()

        inserted_count = 0
        updated_count = 0
        error_count = 0

        for stock in stocks_data:
            try:
                # Extract fields from vnstock API response
                symbol = stock.get('symbol', '')
                name = stock.get('organ_name', stock.get('en_organ_name', ''))
                exchange = stock.get('exchange', 'HOSE')
                stock_type = stock.get('type', '')

                if not symbol:
                    continue

                # Clean exchange name
                exchange = exchange.upper() if exchange else 'HOSE'

                # Categorize stock based on symbol and name
                category = categorize_stock(symbol, name, '', '')

                # Insert or update stock
                cursor.execute("""
                    INSERT INTO stocks (symbol, name, exchange, category, is_active)
                    VALUES (%s, %s, %s, %s, TRUE)
                    ON CONFLICT (symbol)
                    DO UPDATE SET
                        name = EXCLUDED.name,
                        exchange = EXCLUDED.exchange,
                        category = EXCLUDED.category,
                        is_active = TRUE,
                        updated_at = NOW()
                    RETURNING (xmax = 0) AS inserted;
                """, (symbol, name, exchange, category))

                result = cursor.fetchone()
                if result and result[0]:
                    inserted_count += 1
                else:
                    updated_count += 1

                if (inserted_count + updated_count) % 50 == 0:
                    print(f"   Processed {inserted_count + updated_count} stocks...")

            except Exception as e:
                error_count += 1
                print(f"   [WARN]  Error processing {symbol}: {e}")
                continue

        conn.commit()
        cursor.close()
        conn.close()

        print(f"\n[OK] Database population complete!")
        print(f"   New stocks: {inserted_count}")
        print(f"   Updated stocks: {updated_count}")
        if error_count > 0:
            print(f"   Errors: {error_count}")

        return inserted_count + updated_count

    except Exception as e:
        print(f"[ERROR] Database error: {e}")
        return 0


def verify_database():
    """Verify stocks were loaded correctly"""
    print("\n Verifying database...")

    try:
        conn = get_database_connection()
        cursor = conn.cursor()

        # Total stocks
        cursor.execute("SELECT COUNT(*) FROM stocks WHERE is_active = TRUE;")
        total = cursor.fetchone()[0]
        print(f"   Total active stocks: {total}")

        # By exchange
        cursor.execute("""
            SELECT exchange, COUNT(*)
            FROM stocks
            WHERE is_active = TRUE
            GROUP BY exchange
            ORDER BY exchange;
        """)
        print("\n   By exchange:")
        for row in cursor.fetchall():
            print(f"      {row[0]}: {row[1]} stocks")

        # By category
        cursor.execute("""
            SELECT category, COUNT(*)
            FROM stocks
            WHERE is_active = TRUE
            GROUP BY category
            ORDER BY COUNT(*) DESC
            LIMIT 10;
        """)
        print("\n   Top categories:")
        for row in cursor.fetchall():
            print(f"      {row[0]}: {row[1]} stocks")

        cursor.close()
        conn.close()

        return total

    except Exception as e:
        print(f"[ERROR] Verification error: {e}")
        return 0


def main():
    """Main execution"""
    print("=" * 70)
    print(" Loading All Vietnamese Stocks")
    print("=" * 70)

    # Step 1: Fetch all stocks
    stocks_data = get_all_stocks()

    if not stocks_data:
        print("\n[ERROR] Failed to fetch stock data. Exiting.")
        sys.exit(1)

    # Step 2: Populate database
    count = populate_database(stocks_data)

    if count == 0:
        print("\n[ERROR] Failed to populate database. Exiting.")
        sys.exit(1)

    # Step 3: Verify
    total = verify_database()

    print("\n" + "=" * 70)
    print(f"[OK] Success! {total} stocks loaded into database")
    print("=" * 70)
    print("\n Next steps:")
    print("   1. Run data collection:")
    print("      docker compose exec app python jobs/collect_stock_data.py")
    print("   2. Or wait for scheduled collection (hourly during market hours)")
    print()


if __name__ == '__main__':
    main()
