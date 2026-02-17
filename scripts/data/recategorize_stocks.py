#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recategorize stocks based on their sector and industry information
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from config import get_database_connection

def recategorize_stocks():
    """Update stock categories based on sector/industry keywords"""
    print("Recategorizing stocks...")

    conn = get_database_connection()
    cursor = conn.cursor()

    # Fetch all stocks
    cursor.execute("""
        SELECT id, symbol, name, sector, industry
        FROM stocks
        WHERE is_active = TRUE
        ORDER BY symbol;
    """)

    stocks = cursor.fetchall()
    print(f"Processing {len(stocks)} stocks...")

    updates = {
        'banks': 0,
        'securities': 0,
        'insurance': 0,
        'real_estate': 0,
        'construction': 0,
        'tech': 0,
        'telecom': 0,
        'energy': 0,
        'materials': 0,
        'manufacturing': 0,
        'consumer': 0,
        'healthcare': 0,
        'agriculture': 0,
        'transportation': 0,
        'utilities': 0,
        'other': 0
    }

    for stock in stocks:
        stock_id, symbol, name, sector, industry = stock

        # Convert to lowercase for matching
        name_lower = (name or '').lower()
        sector_lower = (sector or '').lower()
        industry_lower = (industry or '').lower()
        combined = f"{name_lower} {sector_lower} {industry_lower}"

        # Determine category
        category = 'other'

        # Banks
        if any(x in combined for x in ['bank', 'ngân hàng', 'banking']):
            category = 'banks'
            updates['banks'] += 1

        # Securities
        elif any(x in combined for x in ['securities', 'chứng khoán', 'brokerage', 'investment']):
            category = 'securities'
            updates['securities'] += 1

        # Insurance
        elif any(x in combined for x in ['insurance', 'bảo hiểm', 'assurance']):
            category = 'insurance'
            updates['insurance'] += 1

        # Real Estate
        elif any(x in combined for x in ['real estate', 'bất động sản', 'property', 'realty', 'land']):
            category = 'real_estate'
            updates['real_estate'] += 1

        # Construction
        elif any(x in combined for x in ['construction', 'xây dựng', 'building', 'infrastructure']):
            category = 'construction'
            updates['construction'] += 1

        # Technology
        elif any(x in combined for x in ['technology', 'công nghệ', 'software', 'it ', 'digital', 'internet']):
            category = 'tech'
            updates['tech'] += 1

        # Telecom
        elif any(x in combined for x in ['telecom', 'viễn thông', 'communication', 'mobile']):
            category = 'telecom'
            updates['telecom'] += 1

        # Energy (Oil & Gas)
        elif any(x in combined for x in ['energy', 'năng lượng', 'oil', 'gas', 'petro', 'petroleum', 'dầu khí']):
            category = 'energy'
            updates['energy'] += 1

        # Materials (Steel, Cement, Chemicals)
        elif any(x in combined for x in ['steel', 'thép', 'cement', 'xi măng', 'chemical', 'hóa chất', 'metal', 'kim loại']):
            category = 'materials'
            updates['materials'] += 1

        # Manufacturing
        elif any(x in combined for x in ['manufacturing', 'sản xuất', 'industrial', 'công nghiệp', 'factory']):
            category = 'manufacturing'
            updates['manufacturing'] += 1

        # Consumer (Retail, Food & Beverage)
        elif any(x in combined for x in ['consumer', 'retail', 'bán lẻ', 'food', 'thực phẩm', 'beverage', 'đồ uống', 'restaurant']):
            category = 'consumer'
            updates['consumer'] += 1

        # Healthcare (Pharma, Medical)
        elif any(x in combined for x in ['healthcare', 'health', 'y tế', 'pharma', 'dược', 'medical', 'hospital', 'bệnh viện']):
            category = 'healthcare'
            updates['healthcare'] += 1

        # Agriculture
        elif any(x in combined for x in ['agriculture', 'nông nghiệp', 'farming', 'fishery', 'thủy sản', 'forestry']):
            category = 'agriculture'
            updates['agriculture'] += 1

        # Transportation
        elif any(x in combined for x in ['transport', 'vận tải', 'logistics', 'shipping', 'airline', 'hàng không']):
            category = 'transportation'
            updates['transportation'] += 1

        # Utilities
        elif any(x in combined for x in ['utilities', 'điện', 'nước', 'electric', 'power', 'water']):
            category = 'utilities'
            updates['utilities'] += 1

        else:
            updates['other'] += 1

        # Update stock category
        cursor.execute("""
            UPDATE stocks
            SET category = %s, updated_at = NOW()
            WHERE id = %s;
        """, (category, stock_id))

    conn.commit()
    cursor.close()
    conn.close()

    print("\n[OK] Recategorization complete!")
    print("\nCategory breakdown:")
    for cat, count in sorted(updates.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"   {cat}: {count} stocks")

    return sum(updates.values())


if __name__ == '__main__':
    total = recategorize_stocks()
    print(f"\nTotal stocks processed: {total}")
