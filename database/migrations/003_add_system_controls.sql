-- Add system control and signals table
-- Allows UI to trigger jobs and manage settings

CREATE TABLE IF NOT EXISTS system_controls (
    id SERIAL PRIMARY KEY,
    control_key VARCHAR(100) UNIQUE NOT NULL,
    control_value TEXT,
    control_type VARCHAR(50) DEFAULT 'setting',  -- 'setting', 'signal', 'state'
    description TEXT,
    updated_at TIMESTAMP DEFAULT NOW(),
    updated_by VARCHAR(100) DEFAULT 'system'
);

-- Create index for fast lookups
CREATE INDEX idx_system_controls_key ON system_controls(control_key);
CREATE INDEX idx_system_controls_type ON system_controls(control_type);

-- Insert initial control settings
INSERT INTO system_controls (control_key, control_value, control_type, description) VALUES
    -- Job Control Signals
    ('job.collect_stock.trigger', 'false', 'signal', 'Trigger stock data collection'),
    ('job.collect_macro.trigger', 'false', 'signal', 'Trigger macro data collection'),
    ('job.scheduler.state', 'stopped', 'state', 'Scheduler running state'),

    -- Collection Settings
    ('collection.stock.enabled', 'true', 'setting', 'Enable stock data collection'),
    ('collection.stock.interval', '3600', 'setting', 'Stock collection interval in seconds'),
    ('collection.indices.enabled', 'true', 'setting', 'Enable market indices collection'),
    ('collection.indices.interval', '1800', 'setting', 'Indices collection interval in seconds'),
    ('collection.macro.enabled', 'true', 'setting', 'Enable macro data collection'),
    ('collection.macro.interval', '3600', 'setting', 'Macro collection interval in seconds'),

    -- Market Hours
    ('market.open_hour', '9', 'setting', 'Market opening hour'),
    ('market.close_hour', '15', 'setting', 'Market closing hour'),
    ('market.days', 'mon-fri', 'setting', 'Trading days'),

    -- System State
    ('system.last_stock_collection', '', 'state', 'Timestamp of last stock collection'),
    ('system.last_macro_collection', '', 'state', 'Timestamp of last macro collection'),
    ('system.collection_status', 'idle', 'state', 'Current collection status')
ON CONFLICT (control_key) DO NOTHING;

-- Create activity log table for monitoring
CREATE TABLE IF NOT EXISTS activity_log (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT NOW(),
    activity_type VARCHAR(50) NOT NULL,  -- 'collection', 'system', 'error', 'info'
    activity VARCHAR(255) NOT NULL,
    details TEXT,
    status VARCHAR(50) DEFAULT 'success'  -- 'success', 'error', 'warning', 'info'
);

-- Create index for fast queries
CREATE INDEX idx_activity_log_timestamp ON activity_log(timestamp DESC);
CREATE INDEX idx_activity_log_type ON activity_log(activity_type);

-- Insert initial log entry
INSERT INTO activity_log (activity_type, activity, details, status) VALUES
    ('system', 'System initialized', 'Control system and activity logging initialized', 'success');

COMMENT ON TABLE system_controls IS 'System-wide controls, settings, and signals for job management';
COMMENT ON TABLE activity_log IS 'Activity log for monitoring system actions and events';
