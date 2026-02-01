#!/bin/bash

echo "=================================================="
echo "Vietnamese Stock Analytics - API Server"
echo "=================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install flask flask-cors
    echo ""
fi

# Generate latest data
echo "📊 Generating latest stock data..."
python3 generate_latest_data.py
echo ""

# Start the API server
echo "✅ Starting API server..."
echo ""
echo "Server will be available at:"
echo "  📍 http://localhost:5000"
echo ""
echo "API Endpoints:"
echo "  🔹 http://localhost:5000/api/stock-categories"
echo "  🔹 http://localhost:5000/api/stock-names"
echo "  🔹 http://localhost:5000/api/watchlist"
echo "  🔹 http://localhost:5000/api/latest"
echo ""
echo "Press CTRL+C to stop the server"
echo "=================================================="
echo ""

python3 api_server.py
