#!/bin/bash
# Stop all servers for Vietnam Stock Analytics Platform

echo "🛑 Stopping all servers..."
echo ""

# Stop servers on specific ports
echo "   Stopping port 5000 (API Server)..."
lsof -ti:5000 | xargs kill -9 2>/dev/null || true

echo "   Stopping port 8888 (Frontend Server)..."
lsof -ti:8888 | xargs kill -9 2>/dev/null || true

# Stop by process name
echo "   Stopping by process name..."
pkill -f "serve_dashboard.py" 2>/dev/null || true
pkill -f "api_server.py" 2>/dev/null || true

sleep 1

echo ""
echo "✅ All servers stopped"
