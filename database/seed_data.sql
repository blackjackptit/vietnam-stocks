-- ═══════════════════════════════════════════════════════════════
-- VNStock Analytics - Seed Data
-- ═══════════════════════════════════════════════════════════════

BEGIN;

-- ═══════════════════════════════════════════════════════════════
-- SEED STOCKS DATA
-- ═══════════════════════════════════════════════════════════════

INSERT INTO stocks (symbol, name, exchange, sector, category, market_cap) VALUES
-- Blue Chips
('VNM', 'Vietnam Dairy Products JSC', 'HOSE', 'Consumer Goods', 'blue_chips', 150000000000),
('VIC', 'Vingroup JSC', 'HOSE', 'Real Estate', 'blue_chips', 200000000000),
('VHM', 'Vinhomes JSC', 'HOSE', 'Real Estate', 'blue_chips', 180000000000),
('VRE', 'Vincom Retail JSC', 'HOSE', 'Real Estate', 'blue_chips', 95000000000),
('HPG', 'Hoa Phat Group JSC', 'HOSE', 'Materials', 'blue_chips', 140000000000),
('MSN', 'Masan Group Corporation', 'HOSE', 'Consumer Goods', 'blue_chips', 120000000000),
('MWG', 'Mobile World Investment Corporation', 'HOSE', 'Consumer Discretionary', 'blue_chips', 85000000000),
('GAS', 'PetroVietnam Gas JSC', 'HOSE', 'Energy', 'blue_chips', 160000000000),

-- Banks
('VCB', 'Vietcombank', 'HOSE', 'Banking', 'banks', 450000000000),
('BID', 'BIDV', 'HOSE', 'Banking', 'banks', 380000000000),
('CTG', 'VietinBank', 'HOSE', 'Banking', 'banks', 350000000000),
('TCB', 'Techcombank', 'HOSE', 'Banking', 'banks', 320000000000),
('MBB', 'MB Bank', 'HOSE', 'Banking', 'banks', 280000000000),
('VPB', 'VPBank', 'HOSE', 'Banking', 'banks', 250000000000),
('ACB', 'Asia Commercial Bank', 'HOSE', 'Banking', 'banks', 200000000000),
('STB', 'Sacombank', 'HOSE', 'Banking', 'banks', 150000000000),

-- Technology
('FPT', 'FPT Corporation', 'HOSE', 'Technology', 'tech', 180000000000),
('CMG', 'CMC Corporation', 'HOSE', 'Technology', 'tech', 25000000000),
('VGI', 'Vietnam Gateway Investment', 'UPCOM', 'Technology', 'tech', 15000000000),

-- Real Estate
('NVL', 'Novaland Group', 'HOSE', 'Real Estate', 'real_estate', 95000000000),
('PDR', 'Phat Dat Real Estate', 'HOSE', 'Real Estate', 'real_estate', 35000000000),
('DXG', 'Dat Xanh Group', 'HOSE', 'Real Estate', 'real_estate', 28000000000),
('KDH', 'Khang Dien House', 'HOSE', 'Real Estate', 'real_estate', 32000000000),

-- Consumer
('SAB', 'Sabeco', 'HOSE', 'Consumer Goods', 'consumer', 125000000000),
('VNM', 'Vinamilk', 'HOSE', 'Consumer Goods', 'consumer', 150000000000),
('MCH', 'Masan Consumer Holdings', 'UPCOM', 'Consumer Goods', 'consumer', 45000000000),

-- Oil & Gas
('PLX', 'Petrolimex', 'HOSE', 'Energy', 'oil_gas', 85000000000),
('PVD', 'PetroVietnam Drilling', 'HOSE', 'Energy', 'oil_gas', 18000000000),
('PVT', 'PetroVietnam Transport', 'HOSE', 'Energy', 'oil_gas', 12000000000),

-- Commodities
('GOLD', 'Gold Price', 'COMMODITY', 'Commodities', 'commodities', NULL),
('OIL', 'Crude Oil', 'COMMODITY', 'Commodities', 'commodities', NULL),
('COPPER', 'Copper', 'COMMODITY', 'Commodities', 'commodities', NULL)

ON CONFLICT (symbol) DO NOTHING;

-- ═══════════════════════════════════════════════════════════════
-- SEED MARKET INDICES
-- ═══════════════════════════════════════════════════════════════

INSERT INTO market_indices (index_code, index_name, date, value, change, change_percent, volume) VALUES
('VN-INDEX', 'Vietnam Ho Chi Minh Stock Index', CURRENT_DATE, 1250.50, 5.30, 0.43, 850000000),
('VN30', 'Vietnam 30 Index', CURRENT_DATE, 1350.75, 6.20, 0.46, 450000000),
('HNX-INDEX', 'Hanoi Stock Exchange Index', CURRENT_DATE, 235.80, 1.50, 0.64, 120000000)
ON CONFLICT (index_code, date) DO NOTHING;

-- ═══════════════════════════════════════════════════════════════
-- SEED MACRO INDICATORS
-- ═══════════════════════════════════════════════════════════════

INSERT INTO macro_indicators (indicator_type, country, date, value, unit, source) VALUES
('gdp_growth', 'VN', '2024-01-01', 6.5, 'percent', 'GSO'),
('inflation', 'VN', '2024-01-01', 3.2, 'percent', 'GSO'),
('interest_rate', 'VN', '2024-01-01', 4.5, 'percent', 'SBV'),
('usd_vnd_rate', 'VN', CURRENT_DATE, 24000.0, 'VND', 'SBV'),
('oil_price', 'WW', CURRENT_DATE, 85.50, 'USD', 'Bloomberg')
ON CONFLICT (indicator_type, country, date) DO NOTHING;

-- ═══════════════════════════════════════════════════════════════
-- SEED SAMPLE USER (For development only - password: admin123)
-- ═══════════════════════════════════════════════════════════════

-- Note: In production, use proper password hashing (bcrypt)
-- This is a bcrypt hash of 'admin123'
INSERT INTO users (email, username, password_hash, full_name, is_admin) VALUES
('admin@vnstock.local', 'admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5zXHovZ8.2aJi', 'Admin User', TRUE),
('demo@vnstock.local', 'demo', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5zXHovZ8.2aJi', 'Demo User', FALSE)
ON CONFLICT (email) DO NOTHING;

-- ═══════════════════════════════════════════════════════════════
-- SEED SAMPLE HISTORICAL PRICES (Last 30 days for VNM)
-- ═══════════════════════════════════════════════════════════════

DO $$
DECLARE
    stock_vnm_id INTEGER;
    i INTEGER;
    base_price DECIMAL := 85000;
    current_date_iter DATE;
BEGIN
    SELECT id INTO stock_vnm_id FROM stocks WHERE symbol = 'VNM';

    IF stock_vnm_id IS NOT NULL THEN
        FOR i IN 0..29 LOOP
            current_date_iter := CURRENT_DATE - i;

            INSERT INTO stock_prices (stock_id, date, open, high, low, close, volume, adjusted_close, change_percent)
            VALUES (
                stock_vnm_id,
                current_date_iter,
                base_price + (random() * 2000 - 1000),
                base_price + (random() * 3000),
                base_price - (random() * 2000),
                base_price + (random() * 2000 - 1000),
                (random() * 5000000 + 1000000)::BIGINT,
                base_price + (random() * 2000 - 1000),
                (random() * 4 - 2)
            )
            ON CONFLICT (stock_id, date) DO NOTHING;

            base_price := base_price + (random() * 1000 - 500);
        END LOOP;
    END IF;
END $$;

COMMIT;

-- ═══════════════════════════════════════════════════════════════
-- SEED DATA COMPLETE
-- ═══════════════════════════════════════════════════════════════

SELECT 'Seed data inserted successfully!' as message;
SELECT COUNT(*) as total_stocks FROM stocks;
SELECT COUNT(*) as total_prices FROM stock_prices;
SELECT COUNT(*) as total_users FROM users;
