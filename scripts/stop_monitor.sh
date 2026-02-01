#!/bin/bash
if [ -f monitor.pid ]; then
    PID=$(cat monitor.pid)
    echo "🛑 Stopping monitor (PID: $PID)..."
    kill $PID 2>/dev/null && echo "✅ Monitor stopped" || echo "⚠️  Process not running"
    rm monitor.pid
else
    echo "🛑 Stopping all demo_monitor processes..."
    pkill -f demo_monitor
    echo "✅ Done"
fi
