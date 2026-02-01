#!/bin/bash
echo "=" * 70
echo "🚀 Starting Enhanced Real-time Stock Dashboard"
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

echo "✅ Enhanced real-time server started (PID: $PID)"
echo ""
echo "🌐 Dashboard URLs:"
echo "   Original: http://localhost:8888/dashboard_realtime.html"
echo "   Enhanced: http://localhost:8888/dashboard_enhanced.html"
echo ""
echo "✨ NEW FEATURES:"
echo "   • Select from ALL Vietnamese stocks (200+ symbols)"
echo "   • Custom watchlist picker"
echo "   • Performance heatmap"
echo "   • Price & volume analysis"
echo "   • Sector distribution chart"
echo "   • Enhanced stock table with detailed metrics"
echo ""
echo "🔄 Make sure monitor is running:"
echo "   python demo_monitor.py --interval 15"
echo ""
echo "📝 Manage watchlist:"
echo "   python manage_watchlist.py --interactive"
echo ""
echo "📝 View logs: tail -f realtime.log"
echo "🛑 Stop server: kill \$(cat realtime.pid)"
echo ""
