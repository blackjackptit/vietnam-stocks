#!/bin/bash
# Run database migrations
# Usage: ./run_migration.sh <migration_file>

cd "$(dirname "$0")"

MIGRATION_FILE=${1:-"migrations/004_add_investment_plans.sql"}

echo "Running migration: $MIGRATION_FILE"

docker compose exec -T postgres psql -U vnstock_user -d vnstock_db < "$MIGRATION_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Migration completed successfully!"
else
    echo "❌ Migration failed!"
    exit 1
fi
