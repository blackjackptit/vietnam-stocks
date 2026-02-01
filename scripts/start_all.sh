#!/bin/bash
# Start ALL servers for Vietnam Stock Analytics Platform

cd "$(dirname "$0")"

echo "============================================================"
echo "🚀 Starting Vietnam Stock Analytics Platform"
echo "============================================================"
echo ""

# Kill existing servers
echo "🧹 Cleaning up old servers..."
lsof -ti:5000 | xargs kill -9 2>/dev/null || true
lsof -ti:8888 | xargs kill -9 2>/dev/null || true
pkill -f "serve_dashboard.py" 2>/dev/null || true
pkill -f "api_server.py" 2>/dev/null || true
sleep 2

# Activate virtual environment
source venv/bin/activate

# Start API Server (port 5000)
echo ""
echo "📡 Starting API Server on port 5000..."
python3 api_server.py > api_server.log 2>&1 &
API_PID=$!
sleep 3

# Check API server
if curl -s http://localhost:5000/health > /dev/null 2>&1; then
    echo "   ✅ API Server running (PID: $API_PID)"
else
    echo "   ❌ API Server failed to start"
    tail -10 api_server.log
    exit 1
fi

# Start Frontend Server (port 8888)
echo ""
echo "🌐 Starting Frontend Server on port 8888..."
python3 serve_dashboard.py > frontend_server.log 2>&1 &
FRONTEND_PID=$!
sleep 3

# Check frontend server
if curl -s http://localhost:8888/index.html > /dev/null 2>&1; then
    echo "   ✅ Frontend Server running (PID: $FRONTEND_PID)"
else
    echo "   ❌ Frontend Server failed to start"
    tail -10 frontend_server.log
    exit 1
fi

echo ""
echo "============================================================"
echo "✅ ALL SERVERS RUNNING"
echo "============================================================"
echo ""
echo "📊 Frontend URLs:"
echo "   http://localhost:8888/index.html (Homepage)"
echo "   http://localhost:8888/dashboard_main.html (Main Dashboard)"
echo "   http://localhost:8888/price_forecast.html (Price Forecast)"
echo "   http://localhost:8888/trading_automation.html (Trading)"
echo ""
echo "🔧 API Endpoints:"
echo "   http://localhost:5000/health (Health Check)"
echo "   http://localhost:5000/api/latest (Latest Data)"
echo "   http://localhost:5000/api/watchlist (Watchlist)"
echo ""
echo "📝 Logs:"
echo "   tail -f api_server.log (API logs)"
echo "   tail -f frontend_server.log (Frontend logs)"
echo ""
echo "🛑 To stop all servers:"
echo "   ./stop_all.sh"
echo ""
echo "============================================================"
