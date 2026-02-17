-- ═══════════════════════════════════════════════════════════════
-- VNStock Analytics - PostgreSQL Database Schema
-- ═══════════════════════════════════════════════════════════════

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm"; -- For text search

-- ═══════════════════════════════════════════════════════════════
-- 1. STOCKS TABLE
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    exchange VARCHAR(50) NOT NULL, -- HOSE, HNX, UPCOM
    sector VARCHAR(100),
    industry VARCHAR(100),
    category VARCHAR(50), -- blue_chips, banks, real_estate, tech, etc.
    market_cap DECIMAL(20, 2),
    shares_outstanding BIGINT,
    is_active BOOLEAN DEFAULT TRUE,
    listed_date DATE,
    metadata JSONB DEFAULT '{}', -- Additional flexible data
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for stocks table
CREATE INDEX idx_stocks_symbol ON stocks(symbol);
CREATE INDEX idx_stocks_exchange ON stocks(exchange);
CREATE INDEX idx_stocks_category ON stocks(category);
CREATE INDEX idx_stocks_sector ON stocks(sector);
CREATE INDEX idx_stocks_active ON stocks(is_active);
CREATE INDEX idx_stocks_name_trgm ON stocks USING gin(name gin_trgm_ops); -- Full-text search

-- ═══════════════════════════════════════════════════════════════
-- 2. STOCK PRICES (Historical OHLCV Data)
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE stock_prices (
    id BIGSERIAL PRIMARY KEY,
    stock_id INTEGER NOT NULL REFERENCES stocks(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    open DECIMAL(15, 2) NOT NULL,
    high DECIMAL(15, 2) NOT NULL,
    low DECIMAL(15, 2) NOT NULL,
    close DECIMAL(15, 2) NOT NULL,
    volume BIGINT NOT NULL DEFAULT 0,
    adjusted_close DECIMAL(15, 2), -- For dividends/splits
    change_percent DECIMAL(10, 4),
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(stock_id, date)
);

-- Indexes for stock_prices table
CREATE INDEX idx_stock_prices_stock_date ON stock_prices(stock_id, date DESC);
CREATE INDEX idx_stock_prices_date ON stock_prices(date DESC);
CREATE INDEX idx_stock_prices_volume ON stock_prices(volume DESC);

-- Partition by date (for better performance with large datasets)
-- Optional: Can be enabled for very large datasets
-- CREATE TABLE stock_prices_2024 PARTITION OF stock_prices
-- FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

-- ═══════════════════════════════════════════════════════════════
-- 3. TECHNICAL INDICATORS
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE technical_indicators (
    id BIGSERIAL PRIMARY KEY,
    stock_id INTEGER NOT NULL REFERENCES stocks(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    -- Moving Averages
    sma_20 DECIMAL(15, 2),
    sma_50 DECIMAL(15, 2),
    sma_200 DECIMAL(15, 2),
    ema_12 DECIMAL(15, 2),
    ema_26 DECIMAL(15, 2),
    -- Momentum Indicators
    rsi_14 DECIMAL(10, 4),
    macd DECIMAL(15, 4),
    macd_signal DECIMAL(15, 4),
    macd_histogram DECIMAL(15, 4),
    stochastic_k DECIMAL(10, 4),
    stochastic_d DECIMAL(10, 4),
    -- Volatility Indicators
    bollinger_upper DECIMAL(15, 2),
    bollinger_middle DECIMAL(15, 2),
    bollinger_lower DECIMAL(15, 2),
    atr_14 DECIMAL(15, 4),
    -- Volume Indicators
    obv BIGINT,
    mfi_14 DECIMAL(10, 4),
    -- Additional indicators as JSON
    indicators JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(stock_id, date)
);

-- Indexes for technical_indicators table
CREATE INDEX idx_tech_indicators_stock_date ON technical_indicators(stock_id, date DESC);

-- ═══════════════════════════════════════════════════════════════
-- 4. PRICE FORECASTS
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE price_forecasts (
    id BIGSERIAL PRIMARY KEY,
    stock_id INTEGER NOT NULL REFERENCES stocks(id) ON DELETE CASCADE,
    forecast_date DATE NOT NULL, -- Date when forecast was made
    target_date DATE NOT NULL, -- Date being predicted
    model_type VARCHAR(50) NOT NULL, -- ensemble, lstm, arima, prophet, etc.
    predicted_price DECIMAL(15, 2) NOT NULL,
    lower_bound DECIMAL(15, 2),
    upper_bound DECIMAL(15, 2),
    confidence DECIMAL(5, 4), -- 0.0 to 1.0
    model_accuracy DECIMAL(5, 4),
    model_parameters JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for price_forecasts table
CREATE INDEX idx_forecasts_stock_target ON price_forecasts(stock_id, target_date DESC);
CREATE INDEX idx_forecasts_date ON price_forecasts(forecast_date DESC);
CREATE INDEX idx_forecasts_model ON price_forecasts(model_type);

-- ═══════════════════════════════════════════════════════════════
-- 5. FORECAST ACCURACY METRICS
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE forecast_accuracy (
    id SERIAL PRIMARY KEY,
    stock_id INTEGER NOT NULL REFERENCES stocks(id) ON DELETE CASCADE,
    model_type VARCHAR(50) NOT NULL,
    evaluation_date DATE NOT NULL,
    mae DECIMAL(15, 4),
    rmse DECIMAL(15, 4),
    mape DECIMAL(10, 4),
    r_squared DECIMAL(10, 6),
    effectiveness_score DECIMAL(5, 2), -- 0-100
    sample_size INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(stock_id, model_type, evaluation_date)
);

-- Indexes for forecast_accuracy table
CREATE INDEX idx_accuracy_stock_model ON forecast_accuracy(stock_id, model_type);
CREATE INDEX idx_accuracy_date ON forecast_accuracy(evaluation_date DESC);

-- ═══════════════════════════════════════════════════════════════
-- 6. USERS (Optional - for authentication)
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid UUID DEFAULT uuid_generate_v4() UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE,
    preferences JSONB DEFAULT '{}', -- User settings
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP
);

-- Indexes for users table
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);

-- ═══════════════════════════════════════════════════════════════
-- 7. USER WATCHLISTS
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE watchlists (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE watchlist_stocks (
    id SERIAL PRIMARY KEY,
    watchlist_id INTEGER NOT NULL REFERENCES watchlists(id) ON DELETE CASCADE,
    stock_id INTEGER NOT NULL REFERENCES stocks(id) ON DELETE CASCADE,
    added_at TIMESTAMP DEFAULT NOW(),
    notes TEXT,
    UNIQUE(watchlist_id, stock_id)
);

-- Indexes for watchlists
CREATE INDEX idx_watchlists_user ON watchlists(user_id);
CREATE INDEX idx_watchlist_stocks_watchlist ON watchlist_stocks(watchlist_id);

-- ═══════════════════════════════════════════════════════════════
-- 8. PRICE ALERTS
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE price_alerts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    stock_id INTEGER NOT NULL REFERENCES stocks(id) ON DELETE CASCADE,
    alert_type VARCHAR(20) NOT NULL, -- above, below, change_percent
    target_price DECIMAL(15, 2),
    target_percent DECIMAL(10, 4),
    is_active BOOLEAN DEFAULT TRUE,
    is_triggered BOOLEAN DEFAULT FALSE,
    triggered_at TIMESTAMP,
    notification_channels JSONB DEFAULT '["email"]', -- email, sms, push
    created_at TIMESTAMP DEFAULT NOW(),
    expires_at TIMESTAMP
);

-- Indexes for price_alerts
CREATE INDEX idx_alerts_user_active ON price_alerts(user_id, is_active);
CREATE INDEX idx_alerts_stock_active ON price_alerts(stock_id, is_active);
CREATE INDEX idx_alerts_triggered ON price_alerts(is_triggered);

-- ═══════════════════════════════════════════════════════════════
-- 9. PORTFOLIOS
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE portfolios (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    initial_capital DECIMAL(20, 2) NOT NULL DEFAULT 0,
    currency VARCHAR(3) DEFAULT 'VND',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE portfolio_positions (
    id SERIAL PRIMARY KEY,
    portfolio_id INTEGER NOT NULL REFERENCES portfolios(id) ON DELETE CASCADE,
    stock_id INTEGER NOT NULL REFERENCES stocks(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL,
    average_price DECIMAL(15, 2) NOT NULL,
    purchase_date DATE,
    current_price DECIMAL(15, 2),
    unrealized_gain_loss DECIMAL(20, 2),
    realized_gain_loss DECIMAL(20, 2) DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(portfolio_id, stock_id)
);

CREATE TABLE portfolio_transactions (
    id SERIAL PRIMARY KEY,
    portfolio_id INTEGER NOT NULL REFERENCES portfolios(id) ON DELETE CASCADE,
    stock_id INTEGER NOT NULL REFERENCES stocks(id) ON DELETE CASCADE,
    transaction_type VARCHAR(10) NOT NULL, -- buy, sell
    quantity INTEGER NOT NULL,
    price DECIMAL(15, 2) NOT NULL,
    total_amount DECIMAL(20, 2) NOT NULL,
    fees DECIMAL(20, 2) DEFAULT 0,
    transaction_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for portfolios
CREATE INDEX idx_portfolios_user ON portfolios(user_id);
CREATE INDEX idx_positions_portfolio ON portfolio_positions(portfolio_id);
CREATE INDEX idx_transactions_portfolio ON portfolio_transactions(portfolio_id);
CREATE INDEX idx_transactions_date ON portfolio_transactions(transaction_date DESC);

-- ═══════════════════════════════════════════════════════════════
-- 10. TRADING STRATEGIES & BACKTESTS
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE trading_strategies (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    strategy_type VARCHAR(50), -- momentum, mean_reversion, ml_based, etc.
    rules JSONB NOT NULL, -- Strategy rules in JSON format
    parameters JSONB DEFAULT '{}',
    is_active BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE backtest_results (
    id SERIAL PRIMARY KEY,
    strategy_id INTEGER NOT NULL REFERENCES trading_strategies(id) ON DELETE CASCADE,
    stock_id INTEGER REFERENCES stocks(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    initial_capital DECIMAL(20, 2) NOT NULL,
    final_capital DECIMAL(20, 2) NOT NULL,
    total_return DECIMAL(15, 4),
    annual_return DECIMAL(15, 4),
    sharpe_ratio DECIMAL(10, 6),
    max_drawdown DECIMAL(15, 4),
    win_rate DECIMAL(5, 4),
    total_trades INTEGER,
    profitable_trades INTEGER,
    metrics JSONB DEFAULT '{}', -- Additional metrics
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for trading strategies
CREATE INDEX idx_strategies_user ON trading_strategies(user_id);
CREATE INDEX idx_backtests_strategy ON backtest_results(strategy_id);

-- ═══════════════════════════════════════════════════════════════
-- 11. MARKET DATA & MACRO INDICATORS
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE market_indices (
    id SERIAL PRIMARY KEY,
    index_code VARCHAR(20) NOT NULL UNIQUE, -- VN-INDEX, VN30, HNX-INDEX
    index_name VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    value DECIMAL(15, 2) NOT NULL,
    change DECIMAL(15, 2),
    change_percent DECIMAL(10, 4),
    volume BIGINT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(index_code, date)
);

CREATE TABLE macro_indicators (
    id SERIAL PRIMARY KEY,
    indicator_type VARCHAR(50) NOT NULL, -- gdp, inflation, interest_rate, oil_price
    country VARCHAR(3) DEFAULT 'VN',
    date DATE NOT NULL,
    value DECIMAL(20, 6) NOT NULL,
    unit VARCHAR(20), -- percent, usd, etc.
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(indicator_type, country, date)
);

-- Indexes for market data
CREATE INDEX idx_market_indices_code_date ON market_indices(index_code, date DESC);
CREATE INDEX idx_macro_indicators_type_date ON macro_indicators(indicator_type, date DESC);

-- ═══════════════════════════════════════════════════════════════
-- 12. AUDIT LOG (Track all important actions)
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE audit_log (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(50) NOT NULL, -- login, forecast_generated, alert_triggered
    entity_type VARCHAR(50), -- stock, portfolio, alert
    entity_id INTEGER,
    details JSONB DEFAULT '{}',
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for audit log
CREATE INDEX idx_audit_user_action ON audit_log(user_id, action, created_at DESC);
CREATE INDEX idx_audit_entity ON audit_log(entity_type, entity_id);
CREATE INDEX idx_audit_created ON audit_log(created_at DESC);

-- ═══════════════════════════════════════════════════════════════
-- VIEWS FOR COMMON QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Latest prices view
CREATE OR REPLACE VIEW latest_stock_prices AS
SELECT DISTINCT ON (s.id)
    s.id as stock_id,
    s.symbol,
    s.name,
    sp.date,
    sp.close as price,
    sp.volume,
    sp.change_percent,
    sp.open,
    sp.high,
    sp.low
FROM stocks s
JOIN stock_prices sp ON s.id = sp.stock_id
WHERE s.is_active = TRUE
ORDER BY s.id, sp.date DESC;

-- Portfolio performance view
CREATE OR REPLACE VIEW portfolio_performance AS
SELECT
    p.id as portfolio_id,
    p.user_id,
    p.name as portfolio_name,
    p.initial_capital,
    SUM(pp.quantity * COALESCE(lsp.price, pp.average_price)) as current_value,
    SUM(pp.unrealized_gain_loss) as total_unrealized_gain_loss,
    SUM(pp.realized_gain_loss) as total_realized_gain_loss,
    (SUM(pp.quantity * COALESCE(lsp.price, pp.average_price)) - p.initial_capital) as total_gain_loss,
    ((SUM(pp.quantity * COALESCE(lsp.price, pp.average_price)) - p.initial_capital) / NULLIF(p.initial_capital, 0) * 100) as return_percent
FROM portfolios p
LEFT JOIN portfolio_positions pp ON p.id = pp.portfolio_id
LEFT JOIN latest_stock_prices lsp ON pp.stock_id = lsp.stock_id
WHERE p.is_active = TRUE
GROUP BY p.id, p.user_id, p.name, p.initial_capital;

-- ═══════════════════════════════════════════════════════════════
-- FUNCTIONS & TRIGGERS
-- ═══════════════════════════════════════════════════════════════

-- Function to update 'updated_at' timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply updated_at trigger to relevant tables
CREATE TRIGGER update_stocks_updated_at BEFORE UPDATE ON stocks
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_portfolios_updated_at BEFORE UPDATE ON portfolios
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_portfolio_positions_updated_at BEFORE UPDATE ON portfolio_positions
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Function to calculate portfolio position unrealized gain/loss
CREATE OR REPLACE FUNCTION calculate_position_gain_loss()
RETURNS TRIGGER AS $$
BEGIN
    NEW.unrealized_gain_loss = (NEW.current_price - NEW.average_price) * NEW.quantity;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_position_gain_loss BEFORE UPDATE ON portfolio_positions
    FOR EACH ROW WHEN (NEW.current_price IS DISTINCT FROM OLD.current_price)
    EXECUTE FUNCTION calculate_position_gain_loss();

-- ═══════════════════════════════════════════════════════════════
-- 17. INVESTMENT PLANS (Dashboard Advanced Feature)
-- ═══════════════════════════════════════════════════════════════

CREATE TABLE investment_plans (
    plan_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    notes TEXT,
    strategy TEXT,
    strategy_name VARCHAR(255),
    budget NUMERIC(15,2),
    expected_return NUMERIC(10,4),
    risk_level NUMERIC(10,4),
    sharpe_ratio NUMERIC(10,4),
    session_id VARCHAR(255) NOT NULL,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE investment_plan_holdings (
    id SERIAL PRIMARY KEY,
    plan_id UUID NOT NULL REFERENCES investment_plans(plan_id) ON DELETE CASCADE,
    symbol VARCHAR(20) NOT NULL,
    shares NUMERIC(15,4),
    buy_price NUMERIC(15,2),
    price_at_creation NUMERIC(15,2),
    allocation_percent NUMERIC(10,4),
    amount NUMERIC(15,2),
    expected_return NUMERIC(10,4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for investment_plans
CREATE INDEX idx_investment_plans_session ON investment_plans(session_id);
CREATE INDEX idx_investment_plan_holdings_plan ON investment_plan_holdings(plan_id);

-- ═══════════════════════════════════════════════════════════════
-- GRANTS (Adjust based on your security requirements)
-- ═══════════════════════════════════════════════════════════════

-- Create roles (uncomment and adjust as needed)
-- CREATE ROLE vnstock_app WITH LOGIN PASSWORD 'your_secure_password';
-- CREATE ROLE vnstock_readonly WITH LOGIN PASSWORD 'your_readonly_password';

-- Grant permissions
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO vnstock_app;
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO vnstock_app;
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO vnstock_readonly;

-- ═══════════════════════════════════════════════════════════════
-- COMMENTS FOR DOCUMENTATION
-- ═══════════════════════════════════════════════════════════════

COMMENT ON TABLE stocks IS 'Master table for all Vietnamese stocks';
COMMENT ON TABLE stock_prices IS 'Historical OHLCV price data for all stocks';
COMMENT ON TABLE technical_indicators IS 'Pre-calculated technical indicators for faster queries';
COMMENT ON TABLE price_forecasts IS 'ML/AI generated price predictions';
COMMENT ON TABLE forecast_accuracy IS 'Model performance metrics for evaluation';
COMMENT ON TABLE users IS 'User accounts and authentication';
COMMENT ON TABLE portfolios IS 'User investment portfolios';
COMMENT ON TABLE price_alerts IS 'Price alert rules and triggers';
COMMENT ON TABLE trading_strategies IS 'User-defined or system trading strategies';
COMMENT ON TABLE audit_log IS 'System-wide audit trail for security and debugging';
COMMENT ON TABLE investment_plans IS 'User-created investment plans with strategy and performance metrics';
COMMENT ON TABLE investment_plan_holdings IS 'Stock allocations within investment plans';

-- ═══════════════════════════════════════════════════════════════
-- SAMPLE DATA (Optional - for development/testing)
-- ═══════════════════════════════════════════════════════════════

-- Insert sample stocks
INSERT INTO stocks (symbol, name, exchange, sector, category) VALUES
('VNM', 'Vinamilk', 'HOSE', 'Consumer Goods', 'blue_chips'),
('VIC', 'Vingroup', 'HOSE', 'Real Estate', 'blue_chips'),
('VCB', 'Vietcombank', 'HOSE', 'Banking', 'banks'),
('FPT', 'FPT Corporation', 'HOSE', 'Technology', 'tech'),
('HPG', 'Hoa Phat Group', 'HOSE', 'Materials', 'blue_chips')
ON CONFLICT (symbol) DO NOTHING;

-- ═══════════════════════════════════════════════════════════════
-- END OF SCHEMA
-- ═══════════════════════════════════════════════════════════════
