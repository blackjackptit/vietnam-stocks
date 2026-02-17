#!/bin/bash
# Docker entrypoint script for Vietnamese Stock Analytics Platform

set -e

echo "======================================================================"
echo "Vietnamese Stock Analytics Platform - Starting..."
echo "======================================================================"

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" 2>/dev/null; do
    echo "PostgreSQL is unavailable - waiting..."
    sleep 2
done
echo "✅ PostgreSQL is ready!"

# Test database connection
echo "Testing database connection..."
python3 - <<EOF
import sys
from config import get_database_connection

try:
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM stocks;")
    count = cursor.fetchone()[0]
    print(f"✅ Database connected: {count} stocks found")
    conn.close()
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    sys.exit(1)
EOF

if [ $? -ne 0 ]; then
    echo "Database connection test failed!"
    exit 1
fi

# Run database initialization if needed
if [ "$RUN_INIT_SCRIPT" = "true" ]; then
    echo "Running database initialization..."
    python scripts/data/sync_data_to_db.py || echo "Warning: Database sync failed"
fi

echo "======================================================================"
echo "Starting application: $@"
echo "======================================================================"

# Execute the provided command
exec "$@"
