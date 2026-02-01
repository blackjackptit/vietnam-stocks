#!/usr/bin/env python3
"""
Macro Economic Data Collection Job
Collects economic indicators and market indices using vnstock
"""

import sys
import os
from datetime import datetime, date, timedelta
from pathlib import Path
import requests
from typing import Dict, Optional

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from vnstock import Vnstock
from config import get_database_connection


class MacroDataCollector:
    """Collects macro economic data from various sources"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.stock = Vnstock()

    def get_vnindex_data(self) -> Optional[Dict]:
        """Get VN-Index data using vnstock"""
        try:
            vn_index = self.stock.stock(symbol='VNINDEX', source='VCI')
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')

            data = vn_index.quote.history(start=start_date, end=end_date)

            if data.empty or len(data) == 0:
                print("  No VNINDEX data available")
                return None

            latest = data.iloc[-1]

            # Calculate change
            change = 0.0
            change_percent = 0.0
            if len(data) >= 2:
                prev_close = float(data.iloc[-2]['close'])
                current_close = float(latest['close'])
                change = current_close - prev_close
                change_percent = (change / prev_close) * 100

            return {
                'index_code': 'VNINDEX',
                'index_name': 'VN-Index',
                'value': float(latest['close']),
                'change': change,
                'change_percent': change_percent,
                'volume': int(latest['volume']),
                'date': date.today()
            }
        except Exception as e:
            print(f"  Error fetching VN-Index: {e}")
        return None

    def get_hnx_index(self) -> Optional[Dict]:
        """Get HNX-Index data using vnstock"""
        try:
            hnx_index = self.stock.stock(symbol='HNX', source='VCI')
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')

            data = hnx_index.quote.history(start=start_date, end=end_date)

            if data.empty or len(data) == 0:
                print("  No HNX data available")
                return None

            latest = data.iloc[-1]

            # Calculate change
            change = 0.0
            change_percent = 0.0
            if len(data) >= 2:
                prev_close = float(data.iloc[-2]['close'])
                current_close = float(latest['close'])
                change = current_close - prev_close
                change_percent = (change / prev_close) * 100

            return {
                'index_code': 'HNX',
                'index_name': 'HNX-Index',
                'value': float(latest['close']),
                'change': change,
                'change_percent': change_percent,
                'volume': int(latest['volume']),
                'date': date.today()
            }
        except Exception as e:
            print(f"  Error fetching HNX-Index: {e}")
        return None

    def get_upcom_index(self) -> Optional[Dict]:
        """Get UPCOM-Index data using vnstock"""
        try:
            upcom_index = self.stock.stock(symbol='UPCOM', source='VCI')
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')

            data = upcom_index.quote.history(start=start_date, end=end_date)

            if data.empty or len(data) == 0:
                print("  No UPCOM data available")
                return None

            latest = data.iloc[-1]

            # Calculate change
            change = 0.0
            change_percent = 0.0
            if len(data) >= 2:
                prev_close = float(data.iloc[-2]['close'])
                current_close = float(latest['close'])
                change = current_close - prev_close
                change_percent = (change / prev_close) * 100

            return {
                'index_code': 'UPCOM',
                'index_name': 'UPCOM-Index',
                'value': float(latest['close']),
                'change': change,
                'change_percent': change_percent,
                'volume': int(latest['volume']),
                'date': date.today()
            }
        except Exception as e:
            print(f"  Error fetching UPCOM-Index: {e}")
        return None

    def get_gold_price(self) -> Optional[Dict]:
        """Get gold price (placeholder - would need real API)"""
        # TODO: Integrate with real gold price API
        # For now, return None to skip
        return None

    def get_oil_price(self) -> Optional[Dict]:
        """Get oil price (placeholder - would need real API)"""
        # TODO: Integrate with commodity price API
        # For now, return None to skip
        return None

    def get_usd_vnd_rate(self) -> Optional[Dict]:
        """Get USD/VND exchange rate"""
        try:
            # VCB API for exchange rates
            url = "https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                # Parse XML response (simplified)
                import xml.etree.ElementTree as ET
                root = ET.fromstring(response.content)

                for exrate in root.findall('.//Exrate'):
                    if exrate.get('CurrencyCode') == 'USD':
                        buy = float(exrate.get('Buy', '0').replace(',', ''))
                        sell = float(exrate.get('Sell', '0').replace(',', ''))
                        transfer = float(exrate.get('Transfer', '0').replace(',', ''))

                        return {
                            'indicator_type': 'usd_vnd',
                            'country': 'VN',
                            'date': date.today(),
                            'value': transfer,  # Use transfer rate
                            'unit': 'VND',
                            'source': 'VCB'
                        }
        except Exception as e:
            print(f"Error fetching USD/VND rate: {e}")
        return None

    def get_interest_rate(self) -> Optional[Dict]:
        """Get Vietnam's benchmark interest rate (placeholder)"""
        # TODO: Integrate with State Bank of Vietnam data
        # For now, return None
        return None

    def collect_market_indices(self):
        """Collect all market indices"""
        print("=" * 70)
        print(f"📊 Collecting Market Indices - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)

        indices = []

        print("Fetching VN-Index...", end=" ", flush=True)
        vnindex = self.get_vnindex_data()
        if vnindex:
            indices.append(vnindex)
            print(f"✓ {vnindex['value']}")
        else:
            print("✗")

        print("Fetching HNX-Index...", end=" ", flush=True)
        hnx = self.get_hnx_index()
        if hnx:
            indices.append(hnx)
            print(f"✓ {hnx['value']}")
        else:
            print("✗")

        print("Fetching UPCOM-Index...", end=" ", flush=True)
        upcom = self.get_upcom_index()
        if upcom:
            indices.append(upcom)
            print(f"✓ {upcom['value']}")
        else:
            print("✗")

        print(f"\n✅ Collected {len(indices)} market indices")
        return indices

    def collect_macro_indicators(self):
        """Collect macro economic indicators"""
        print("\n" + "=" * 70)
        print(f"📈 Collecting Macro Indicators - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)

        indicators = []

        print("Fetching USD/VND rate...", end=" ", flush=True)
        usd_vnd = self.get_usd_vnd_rate()
        if usd_vnd:
            indicators.append(usd_vnd)
            print(f"✓ {usd_vnd['value']:,.0f}")
        else:
            print("✗")

        print(f"\n✅ Collected {len(indicators)} macro indicators")
        return indicators

    def save_indices_to_database(self, indices):
        """Save market indices to database"""
        if not indices:
            return

        try:
            conn = get_database_connection()
            print(f"\n💾 Saving {len(indices)} indices to database...")

            with conn.cursor() as cursor:
                for idx in indices:
                    cursor.execute("""
                        INSERT INTO market_indices
                            (index_code, index_name, value, change, change_percent, volume, date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (index_code, date)
                        DO UPDATE SET
                            value = EXCLUDED.value,
                            change = EXCLUDED.change,
                            change_percent = EXCLUDED.change_percent,
                            volume = EXCLUDED.volume
                    """, (
                        idx['index_code'],
                        idx['index_name'],
                        idx['value'],
                        idx['change'],
                        idx['change_percent'],
                        idx['volume'],
                        idx['date']
                    ))

                conn.commit()
                print(f"✅ Saved {len(indices)} indices")

            conn.close()

        except Exception as e:
            print(f"❌ Database error: {e}")
            if conn:
                conn.rollback()
                conn.close()

    def save_indicators_to_database(self, indicators):
        """Save macro indicators to database"""
        if not indicators:
            return

        try:
            conn = get_database_connection()
            print(f"\n💾 Saving {len(indicators)} indicators to database...")

            with conn.cursor() as cursor:
                for ind in indicators:
                    cursor.execute("""
                        INSERT INTO macro_indicators
                            (indicator_type, country, date, value, unit, source)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ON CONFLICT (indicator_type, country, date)
                        DO UPDATE SET
                            value = EXCLUDED.value,
                            unit = EXCLUDED.unit,
                            source = EXCLUDED.source
                    """, (
                        ind['indicator_type'],
                        ind['country'],
                        ind['date'],
                        ind['value'],
                        ind['unit'],
                        ind['source']
                    ))

                conn.commit()
                print(f"✅ Saved {len(indicators)} indicators")

            conn.close()

        except Exception as e:
            print(f"❌ Database error: {e}")
            if conn:
                conn.rollback()
                conn.close()

    def run(self):
        """Run the macro data collection job"""
        try:
            # Collect market indices
            indices = self.collect_market_indices()
            if indices:
                self.save_indices_to_database(indices)

            # Collect macro indicators
            indicators = self.collect_macro_indicators()
            if indicators:
                self.save_indicators_to_database(indicators)

            print(f"\n✅ Macro data collection completed at {datetime.now().strftime('%H:%M:%S')}")

        except Exception as e:
            print(f"\n❌ Job failed: {e}")
            raise


def main():
    """Main entry point"""
    collector = MacroDataCollector()
    collector.run()


if __name__ == '__main__':
    main()
