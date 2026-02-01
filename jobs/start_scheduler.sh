#!/bin/bash
# Start the data collection scheduler

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Starting Stock Data Scheduler..."
echo "Project directory: $PROJECT_DIR"

cd "$PROJECT_DIR"

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✓ Virtual environment activated"
else
    echo "⚠️  Warning: No virtual environment found"
fi

# Install required packages if needed
pip install -q APScheduler psycopg2-binary 2>/dev/null

# Run the scheduler
python jobs/scheduler.py

# Deactivate virtual environment
deactivate 2>/dev/null
