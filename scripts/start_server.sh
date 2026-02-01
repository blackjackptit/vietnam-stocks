#!/bin/bash
# Start API Server for Vietnam Stock Analytics Platform

cd "$(dirname "$0")"

# Kill any existing server on port 5000
echo "Checking for existing server..."
lsof -ti:5000 | xargs kill -9 2>/dev/null || true
sleep 1

# Activate virtual environment
source venv/bin/activate

# Start server
echo "Starting API server on http://localhost:5000"
python3 api_server.py > api_server.log 2>&1 &

# Wait and check if server started
sleep 3
if curl -s http://localhost:5000/health > /dev/null 2>&1; then
    echo "✅ API Server started successfully!"
    echo "   Health: http://localhost:5000/health"
    echo "   Latest: http://localhost:5000/api/latest"
    echo ""
    echo "Logs: tail -f api_server.log"
else
    echo "❌ Server failed to start. Check api_server.log"
    tail -20 api_server.log
    exit 1
fi
