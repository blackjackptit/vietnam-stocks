-- ═══════════════════════════════════════════════════════════════
-- VNStock Analytics - Common SQL Queries
-- ═══════════════════════════════════════════════════════════════

-- ═══════════════════════════════════════════════════════════════
-- 1. STOCK QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Get all active stocks with latest price
SELECT
    s.symbol,
    s.name,
    s.exchange,
    s.sector,
    lsp.price as current_price,
    lsp.change_percent,
    lsp.volume,
    lsp.date as last_updated
FROM stocks s
LEFT JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE s.is_active = TRUE
ORDER BY s.symbol;

-- Get stock price history (last 30 days)
SELECT
    s.symbol,
    sp.date,
    sp.open,
    sp.high,
    sp.low,
    sp.close,
    sp.volume,
    sp.change_percent
FROM stock_prices sp
JOIN stocks s ON sp.stock_id = s.id
WHERE s.symbol = 'VNM'
    AND sp.date >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY sp.date DESC;

-- Search stocks by name or symbol
SELECT
    symbol,
    name,
    exchange,
    sector,
    category
FROM stocks
WHERE
    (name ILIKE '%vinamilk%' OR symbol ILIKE '%vnm%')
    AND is_active = TRUE
ORDER BY
    CASE WHEN symbol ILIKE 'vnm%' THEN 1 ELSE 2 END,
    symbol;

-- Get top gainers today
SELECT
    s.symbol,
    s.name,
    sp.close as price,
    sp.change_percent,
    sp.volume
FROM stock_prices sp
JOIN stocks s ON sp.stock_id = s.id
WHERE sp.date = CURRENT_DATE
ORDER BY sp.change_percent DESC
LIMIT 10;

-- Get top losers today
SELECT
    s.symbol,
    s.name,
    sp.close as price,
    sp.change_percent,
    sp.volume
FROM stock_prices sp
JOIN stocks s ON sp.stock_id = s.id
WHERE sp.date = CURRENT_DATE
ORDER BY sp.change_percent ASC
LIMIT 10;

-- Get most active by volume
SELECT
    s.symbol,
    s.name,
    sp.close as price,
    sp.volume,
    sp.change_percent
FROM stock_prices sp
JOIN stocks s ON sp.stock_id = s.id
WHERE sp.date = CURRENT_DATE
ORDER BY sp.volume DESC
LIMIT 10;

-- ═══════════════════════════════════════════════════════════════
-- 2. TECHNICAL INDICATOR QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Get latest technical indicators for a stock
SELECT
    s.symbol,
    ti.date,
    ti.sma_20,
    ti.sma_50,
    ti.sma_200,
    ti.rsi_14,
    ti.macd,
    ti.macd_signal,
    ti.bollinger_upper,
    ti.bollinger_middle,
    ti.bollinger_lower
FROM technical_indicators ti
JOIN stocks s ON ti.stock_id = s.id
WHERE s.symbol = 'VNM'
ORDER BY ti.date DESC
LIMIT 1;

-- Find stocks with RSI < 30 (oversold)
SELECT
    s.symbol,
    s.name,
    ti.rsi_14,
    lsp.price,
    lsp.change_percent
FROM technical_indicators ti
JOIN stocks s ON ti.stock_id = s.id
LEFT JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE ti.date = (SELECT MAX(date) FROM technical_indicators)
    AND ti.rsi_14 < 30
ORDER BY ti.rsi_14 ASC;

-- Find stocks with golden cross (SMA 50 > SMA 200)
SELECT
    s.symbol,
    s.name,
    ti.sma_50,
    ti.sma_200,
    lsp.price,
    lsp.change_percent
FROM technical_indicators ti
JOIN stocks s ON ti.stock_id = s.id
LEFT JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE ti.date = (SELECT MAX(date) FROM technical_indicators)
    AND ti.sma_50 > ti.sma_200
    AND ti.sma_50 IS NOT NULL
    AND ti.sma_200 IS NOT NULL
ORDER BY (ti.sma_50 - ti.sma_200) DESC;

-- ═══════════════════════════════════════════════════════════════
-- 3. FORECAST QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Get latest forecasts for a stock
SELECT
    s.symbol,
    pf.target_date,
    pf.model_type,
    pf.predicted_price,
    pf.lower_bound,
    pf.upper_bound,
    pf.confidence,
    pf.forecast_date
FROM price_forecasts pf
JOIN stocks s ON pf.stock_id = s.id
WHERE s.symbol = 'VNM'
    AND pf.target_date >= CURRENT_DATE
ORDER BY pf.target_date, pf.model_type;

-- Compare forecast accuracy across models
SELECT
    s.symbol,
    fa.model_type,
    fa.mae,
    fa.rmse,
    fa.mape,
    fa.r_squared,
    fa.effectiveness_score,
    fa.evaluation_date
FROM forecast_accuracy fa
JOIN stocks s ON fa.stock_id = s.id
WHERE s.symbol = 'VNM'
ORDER BY fa.evaluation_date DESC, fa.effectiveness_score DESC;

-- Get best performing forecast model by stock
SELECT DISTINCT ON (s.symbol)
    s.symbol,
    s.name,
    fa.model_type as best_model,
    fa.effectiveness_score,
    fa.mape,
    fa.r_squared
FROM forecast_accuracy fa
JOIN stocks s ON fa.stock_id = s.id
WHERE fa.evaluation_date = (SELECT MAX(evaluation_date) FROM forecast_accuracy)
ORDER BY s.symbol, fa.effectiveness_score DESC;

-- ═══════════════════════════════════════════════════════════════
-- 4. PORTFOLIO QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Get user portfolio summary
SELECT * FROM portfolio_performance
WHERE user_id = 1
ORDER BY total_gain_loss DESC;

-- Get detailed portfolio positions
SELECT
    p.name as portfolio_name,
    s.symbol,
    s.name as stock_name,
    pp.quantity,
    pp.average_price,
    lsp.price as current_price,
    pp.unrealized_gain_loss,
    pp.realized_gain_loss,
    (pp.quantity * lsp.price) as current_value,
    ((lsp.price - pp.average_price) / NULLIF(pp.average_price, 0) * 100) as return_percent
FROM portfolio_positions pp
JOIN portfolios p ON pp.portfolio_id = p.id
JOIN stocks s ON pp.stock_id = s.id
LEFT JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE p.user_id = 1
ORDER BY pp.unrealized_gain_loss DESC;

-- Get portfolio transaction history
SELECT
    pt.transaction_date,
    s.symbol,
    s.name,
    pt.transaction_type,
    pt.quantity,
    pt.price,
    pt.total_amount,
    pt.fees,
    pt.notes
FROM portfolio_transactions pt
JOIN stocks s ON pt.stock_id = s.id
JOIN portfolios p ON pt.portfolio_id = p.id
WHERE p.user_id = 1
ORDER BY pt.transaction_date DESC
LIMIT 50;

-- Calculate portfolio sector allocation
SELECT
    s.sector,
    COUNT(DISTINCT pp.stock_id) as num_stocks,
    SUM(pp.quantity * lsp.price) as total_value,
    (SUM(pp.quantity * lsp.price) / NULLIF(SUM(SUM(pp.quantity * lsp.price)) OVER(), 0) * 100) as allocation_percent
FROM portfolio_positions pp
JOIN portfolios p ON pp.portfolio_id = p.id
JOIN stocks s ON pp.stock_id = s.id
LEFT JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE p.user_id = 1
GROUP BY s.sector
ORDER BY total_value DESC;

-- ═══════════════════════════════════════════════════════════════
-- 5. ALERT QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Get active price alerts
SELECT
    pa.id,
    s.symbol,
    s.name,
    pa.alert_type,
    pa.target_price,
    pa.target_percent,
    lsp.price as current_price,
    pa.created_at
FROM price_alerts pa
JOIN stocks s ON pa.stock_id = s.id
LEFT JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE pa.user_id = 1
    AND pa.is_active = TRUE
    AND pa.is_triggered = FALSE
ORDER BY pa.created_at DESC;

-- Check if any alerts should be triggered
SELECT
    pa.id as alert_id,
    pa.user_id,
    s.symbol,
    pa.alert_type,
    pa.target_price,
    lsp.price as current_price,
    CASE
        WHEN pa.alert_type = 'above' AND lsp.price >= pa.target_price THEN TRUE
        WHEN pa.alert_type = 'below' AND lsp.price <= pa.target_price THEN TRUE
        ELSE FALSE
    END as should_trigger
FROM price_alerts pa
JOIN stocks s ON pa.stock_id = s.id
JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE pa.is_active = TRUE
    AND pa.is_triggered = FALSE
    AND (
        (pa.alert_type = 'above' AND lsp.price >= pa.target_price)
        OR (pa.alert_type = 'below' AND lsp.price <= pa.target_price)
    );

-- ═══════════════════════════════════════════════════════════════
-- 6. WATCHLIST QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Get user watchlists with stock count
SELECT
    w.id,
    w.name,
    w.description,
    w.is_default,
    COUNT(ws.stock_id) as stock_count,
    w.created_at
FROM watchlists w
LEFT JOIN watchlist_stocks ws ON w.id = ws.watchlist_id
WHERE w.user_id = 1
GROUP BY w.id
ORDER BY w.is_default DESC, w.name;

-- Get stocks in a watchlist with current prices
SELECT
    s.symbol,
    s.name,
    s.sector,
    lsp.price,
    lsp.change_percent,
    lsp.volume,
    ws.added_at,
    ws.notes
FROM watchlist_stocks ws
JOIN stocks s ON ws.stock_id = s.id
LEFT JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE ws.watchlist_id = 1
ORDER BY ws.added_at DESC;

-- ═══════════════════════════════════════════════════════════════
-- 7. MARKET OVERVIEW QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Get latest market indices
SELECT
    index_code,
    index_name,
    value,
    change,
    change_percent,
    volume,
    date
FROM market_indices
WHERE date = (SELECT MAX(date) FROM market_indices)
ORDER BY index_code;

-- Get macro indicators trends (last 12 months)
SELECT
    indicator_type,
    date,
    value,
    unit
FROM macro_indicators
WHERE indicator_type IN ('gdp_growth', 'inflation', 'interest_rate')
    AND date >= CURRENT_DATE - INTERVAL '12 months'
ORDER BY indicator_type, date DESC;

-- Market summary statistics
SELECT
    COUNT(DISTINCT s.id) as total_stocks,
    COUNT(DISTINCT CASE WHEN sp.change_percent > 0 THEN s.id END) as gainers,
    COUNT(DISTINCT CASE WHEN sp.change_percent < 0 THEN s.id END) as losers,
    COUNT(DISTINCT CASE WHEN sp.change_percent = 0 THEN s.id END) as unchanged,
    SUM(sp.volume) as total_volume,
    AVG(sp.change_percent) as avg_change_percent
FROM stocks s
JOIN stock_prices sp ON s.id = sp.stock_id
WHERE sp.date = CURRENT_DATE
    AND s.is_active = TRUE;

-- ═══════════════════════════════════════════════════════════════
-- 8. ANALYTICS & REPORTING QUERIES
-- ═══════════════════════════════════════════════════════════════

-- Stock volatility analysis (30-day)
SELECT
    s.symbol,
    s.name,
    AVG(sp.close) as avg_price,
    STDDEV(sp.close) as price_stddev,
    (STDDEV(sp.close) / NULLIF(AVG(sp.close), 0) * 100) as coefficient_of_variation,
    MAX(sp.high) as period_high,
    MIN(sp.low) as period_low,
    ((MAX(sp.high) - MIN(sp.low)) / NULLIF(MIN(sp.low), 0) * 100) as price_range_percent
FROM stock_prices sp
JOIN stocks s ON sp.stock_id = s.id
WHERE sp.date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY s.id, s.symbol, s.name
ORDER BY coefficient_of_variation DESC
LIMIT 20;

-- Sector performance comparison
SELECT
    s.sector,
    COUNT(DISTINCT s.id) as num_stocks,
    AVG(sp.change_percent) as avg_change_percent,
    SUM(sp.volume) as total_volume,
    AVG(s.market_cap) as avg_market_cap
FROM stocks s
JOIN stock_prices sp ON s.id = sp.stock_id
WHERE sp.date = CURRENT_DATE
    AND s.sector IS NOT NULL
GROUP BY s.sector
ORDER BY avg_change_percent DESC;

-- ═══════════════════════════════════════════════════════════════
-- END OF QUERIES
-- ═══════════════════════════════════════════════════════════════
