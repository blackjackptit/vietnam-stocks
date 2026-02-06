-- Add investment plans table for portfolio tracking
-- Stores user-created investment plans with performance tracking

CREATE TABLE IF NOT EXISTS investment_plans (
    id SERIAL PRIMARY KEY,
    plan_id UUID DEFAULT uuid_generate_v4() UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    notes TEXT,
    strategy VARCHAR(100),  -- 'balanced', 'growth', 'conservative', 'bluechip', 'manual'
    strategy_name VARCHAR(255),
    budget DECIMAL(20, 2) NOT NULL,
    expected_return DECIMAL(10, 4),
    risk_level DECIMAL(10, 4),
    sharpe_ratio DECIMAL(10, 4),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    session_id VARCHAR(255),  -- Optional: link to user session
    metadata JSONB DEFAULT '{}'
);

-- Table for individual holdings in each plan
CREATE TABLE IF NOT EXISTS investment_plan_holdings (
    id SERIAL PRIMARY KEY,
    plan_id UUID NOT NULL REFERENCES investment_plans(plan_id) ON DELETE CASCADE,
    symbol VARCHAR(10) NOT NULL,
    shares DECIMAL(15, 4) NOT NULL,
    buy_price DECIMAL(15, 2) NOT NULL,
    price_at_creation DECIMAL(15, 2),  -- Price when plan was created (for comparison)
    allocation_percent DECIMAL(10, 4),
    amount DECIMAL(20, 2),
    expected_return DECIMAL(10, 4),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for fast queries
CREATE INDEX idx_investment_plans_plan_id ON investment_plans(plan_id);
CREATE INDEX idx_investment_plans_session ON investment_plans(session_id);
CREATE INDEX idx_investment_plans_created ON investment_plans(created_at DESC);
CREATE INDEX idx_plan_holdings_plan_id ON investment_plan_holdings(plan_id);
CREATE INDEX idx_plan_holdings_symbol ON investment_plan_holdings(symbol);

-- Insert initial log entry
INSERT INTO activity_log (activity_type, activity, details, status) VALUES
    ('system', 'Investment plans feature initialized', 'Investment plans and holdings tables created', 'success');

COMMENT ON TABLE investment_plans IS 'User-created investment plans for portfolio tracking and performance comparison';
COMMENT ON TABLE investment_plan_holdings IS 'Individual stock holdings within each investment plan';
