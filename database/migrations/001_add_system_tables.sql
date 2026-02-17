-- Migration: Add system_controls and activity_log tables
-- Date: 2026-02-17
-- Description: Add missing tables for system controls and activity logging

-- ═══════════════════════════════════════════════════════════════
-- SYSTEM CONTROLS TABLE
-- ═══════════════════════════════════════════════════════════════
CREATE TABLE IF NOT EXISTS system_controls (
    id SERIAL PRIMARY KEY,
    control_key VARCHAR(100) NOT NULL UNIQUE,
    control_value TEXT NOT NULL,
    control_type VARCHAR(20) NOT NULL, -- setting, signal, state
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Index for system_controls
CREATE INDEX IF NOT EXISTS idx_system_controls_key ON system_controls(control_key);
CREATE INDEX IF NOT EXISTS idx_system_controls_type ON system_controls(control_type);

-- Insert default system controls
INSERT INTO system_controls (control_key, control_value, control_type, description) VALUES
-- Job trigger signals
('job.collect_stock.trigger', 'false', 'signal', 'Trigger stock data collection job'),
('job.collect_macro.trigger', 'false', 'signal', 'Trigger macro data collection job'),

-- Data collection settings
('data.auto_collect_enabled', 'true', 'setting', 'Enable automatic data collection'),
('data.stock_collection_enabled', 'true', 'setting', 'Enable stock data collection'),
('data.macro_collection_enabled', 'true', 'setting', 'Enable macro data collection'),

-- System states
('system.scheduler_running', 'false', 'state', 'Scheduler service running status'),
('system.last_stock_collection', '', 'state', 'Last stock data collection timestamp'),
('system.last_macro_collection', '', 'state', 'Last macro data collection timestamp')
ON CONFLICT (control_key) DO NOTHING;

-- ═══════════════════════════════════════════════════════════════
-- ACTIVITY LOG TABLE
-- ═══════════════════════════════════════════════════════════════
CREATE TABLE IF NOT EXISTS activity_log (
    id BIGSERIAL PRIMARY KEY,
    activity_type VARCHAR(50) NOT NULL, -- system, collection, user, alert, etc.
    activity VARCHAR(100) NOT NULL,
    details TEXT,
    status VARCHAR(20) DEFAULT 'info', -- info, warning, error, success
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    metadata JSONB DEFAULT '{}',
    timestamp TIMESTAMP DEFAULT NOW()
);

-- Indexes for activity_log
CREATE INDEX IF NOT EXISTS idx_activity_log_type ON activity_log(activity_type);
CREATE INDEX IF NOT EXISTS idx_activity_log_timestamp ON activity_log(timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_activity_log_status ON activity_log(status);
CREATE INDEX IF NOT EXISTS idx_activity_log_user ON activity_log(user_id);

-- Trigger for system_controls updated_at
DROP TRIGGER IF EXISTS update_system_controls_updated_at ON system_controls;
CREATE TRIGGER update_system_controls_updated_at
BEFORE UPDATE ON system_controls
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

COMMENT ON TABLE system_controls IS 'System configuration controls and settings';
COMMENT ON TABLE activity_log IS 'Activity and event logging for monitoring';

-- Insert initial activity log entry
INSERT INTO activity_log (activity_type, activity, details, status)
VALUES ('system', 'Database migration', 'Added system_controls and activity_log tables', 'success');
