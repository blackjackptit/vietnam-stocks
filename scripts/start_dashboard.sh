#!/bin/bash
echo "🚀 Starting Vietnamese Stock Monitor Dashboard..."
echo ""

# Check if scan data exists
if [ ! -d "output" ] || [ -z "$(ls -A output/*.json 2>/dev/null)" ]; then
    echo "⚠️  No scan data found. Running a scan first..."
    python3 demo_monitor.py --scan-once
    echo ""
fi

# Start the dashboard server
python3 serve_dashboard.py
