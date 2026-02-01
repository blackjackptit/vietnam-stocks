#!/bin/bash
echo "=" * 70
echo "🚀 Starting Real-time Stock Dashboard"
echo "=" * 70
echo ""

# Kill any existing servers
lsof -ti:8888 | xargs kill -9 2>/dev/null
sleep 1

# Start real-time server
nohup python3 realtime_server.py > realtime.log 2>&1 &
PID=$!
echo $PID > realtime.pid

sleep 2

echo "✅ Real-time server started (PID: $PID)"
echo ""
echo "🌐 Dashboard URL: http://localhost:8888/dashboard_realtime.html"
echo ""
echo "📊 Features:"
echo "   • Updates every 2 seconds"
echo "   • Live charts and graphs"
echo "   • Instant data refresh when scans complete"
echo ""
echo "🔄 Make sure monitor is running:"
echo "   python demo_monitor.py --interval 15"
echo ""
echo "📝 View logs: tail -f realtime.log"
echo "🛑 Stop server: kill $(cat realtime.pid)"
echo ""
