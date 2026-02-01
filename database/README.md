# VNStock Analytics - PostgreSQL Database

Complete PostgreSQL database setup for the VNStock Analytics platform.

## 📋 Database Overview

### Tables

1. **stocks** - Master table for all Vietnamese stocks
2. **stock_prices** - Historical OHLCV price data
3. **technical_indicators** - Pre-calculated technical indicators
4. **price_forecasts** - ML/AI generated price predictions
5. **forecast_accuracy** - Model performance metrics
6. **users** - User accounts and authentication
7. **watchlists** - User stock watchlists
8. **watchlist_stocks** - Stocks in watchlists
9. **price_alerts** - Price alert rules
10. **portfolios** - User investment portfolios
11. **portfolio_positions** - Current portfolio holdings
12. **portfolio_transactions** - Portfolio trade history
13. **trading_strategies** - User-defined trading strategies
14. **backtest_results** - Strategy backtesting results
15. **market_indices** - Market index data (VN-INDEX, VN30, etc.)
16. **macro_indicators** - Economic indicators
17. **audit_log** - System audit trail

### Views

- **latest_stock_prices** - Quick access to current stock prices
- **portfolio_performance** - Calculated portfolio returns

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
# 1. Navigate to database directory
cd database

# 2. Start PostgreSQL with Docker Compose
docker-compose up -d

# 3. Check if containers are running
docker-compose ps

# 4. View logs
docker-compose logs -f postgres
```

**Access Points:**
- PostgreSQL: `localhost:5432`
- PgAdmin: `http://localhost:5050`
  - Email: `admin@vnstock.com`
  - Password: `admin123`

### Option 2: Local PostgreSQL Installation

```bash
# 1. Install PostgreSQL (if not already installed)
# macOS
brew install postgresql@15

# Ubuntu/Debian
sudo apt install postgresql-15

# 2. Create database
createdb vnstock_db

# 3. Run schema
psql -U postgres -d vnstock_db -f schema.sql

# 4. Load seed data
psql -U postgres -d vnstock_db -f seed_data.sql
```

## 🔧 Configuration

### Database Connection

**Default Configuration:**
```
Host: localhost
Port: 5432
Database: vnstock_db
User: vnstock_user
Password: vnstock_password_change_in_production
```

### Python Connection Example

```python
import psycopg2
from psycopg2.extras import RealDictCursor

# Connection parameters
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="vnstock_db",
    user="vnstock_user",
    password="vnstock_password_change_in_production"
)

# Query example
with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute("""
        SELECT symbol, name, close as price, change_percent
        FROM latest_stock_prices
        ORDER BY change_percent DESC
        LIMIT 10
    """)
    top_gainers = cursor.fetchall()

conn.close()
```

### Node.js Connection Example

```javascript
const { Pool } = require('pg');

const pool = new Pool({
  host: 'localhost',
  port: 5432,
  database: 'vnstock_db',
  user: 'vnstock_user',
  password: 'vnstock_password_change_in_production',
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

// Query example
async function getTopGainers() {
  const result = await pool.query(`
    SELECT symbol, name, close as price, change_percent
    FROM latest_stock_prices
    ORDER BY change_percent DESC
    LIMIT 10
  `);
  return result.rows;
}
```

## 📊 Schema Diagram

```
┌─────────────┐
│   stocks    │
└──────┬──────┘
       │
       ├─────┬─────────────────────┐
       │     │                     │
       ↓     ↓                     ↓
┌──────────────┐  ┌──────────────────┐  ┌───────────────────┐
│ stock_prices │  │ technical_        │  │ price_forecasts   │
│              │  │ indicators        │  │                   │
└──────────────┘  └──────────────────┘  └───────────────────┘

       ↓
┌───────────────────┐
│ forecast_accuracy │
└───────────────────┘

┌─────────────┐
│    users    │
└──────┬──────┘
       │
       ├─────┬──────────────┬─────────────────┐
       │     │              │                 │
       ↓     ↓              ↓                 ↓
┌────────────┐  ┌──────────────┐  ┌────────────────┐
│ watchlists │  │ portfolios   │  │ price_alerts   │
└─────┬──────┘  └──────┬───────┘  └────────────────┘
      │                │
      ↓                ├────────┬──────────────────┐
┌──────────────┐       ↓        ↓                  ↓
│ watchlist_   │  ┌─────────────────┐  ┌──────────────────────┐
│ stocks       │  │ portfolio_      │  │ portfolio_           │
└──────────────┘  │ positions       │  │ transactions         │
                  └─────────────────┘  └──────────────────────┘
```

## 📝 Common Queries

### Get Latest Stock Prices

```sql
SELECT symbol, name, price, change_percent, volume
FROM latest_stock_prices
ORDER BY change_percent DESC;
```

### Get Stock History

```sql
SELECT date, open, high, low, close, volume
FROM stock_prices
WHERE stock_id = (SELECT id FROM stocks WHERE symbol = 'VNM')
  AND date >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY date DESC;
```

### Search Stocks

```sql
SELECT symbol, name, sector, category
FROM stocks
WHERE (name ILIKE '%vinamilk%' OR symbol ILIKE '%vnm%')
  AND is_active = TRUE;
```

### Get Portfolio Performance

```sql
SELECT * FROM portfolio_performance
WHERE user_id = 1;
```

### Check Active Alerts

```sql
SELECT pa.*, s.symbol, lsp.price as current_price
FROM price_alerts pa
JOIN stocks s ON pa.stock_id = s.id
LEFT JOIN latest_stock_prices lsp ON s.id = lsp.stock_id
WHERE pa.user_id = 1
  AND pa.is_active = TRUE
  AND pa.is_triggered = FALSE;
```

See `queries.sql` for more examples.

## 🔐 Security

### Production Recommendations

1. **Change Default Passwords:**
   ```sql
   ALTER USER vnstock_user WITH PASSWORD 'your_secure_password';
   ```

2. **Create Read-Only User:**
   ```sql
   CREATE ROLE vnstock_readonly WITH LOGIN PASSWORD 'readonly_password';
   GRANT SELECT ON ALL TABLES IN SCHEMA public TO vnstock_readonly;
   ```

3. **Enable SSL:**
   ```
   ssl = on
   ssl_cert_file = 'server.crt'
   ssl_key_file = 'server.key'
   ```

4. **Configure pg_hba.conf:**
   ```
   # Only allow local connections
   host    vnstock_db    vnstock_user    127.0.0.1/32    scram-sha-256
   ```

5. **Backup Strategy:**
   ```bash
   # Automated daily backups
   pg_dump -U vnstock_user vnstock_db | gzip > backup_$(date +%Y%m%d).sql.gz
   ```

## 🔄 Migrations

### Create New Migration

```bash
# Create new migration file
touch migrations/002_add_new_feature.sql
```

Example migration:
```sql
-- Migration: 002_add_new_feature
-- Description: Add new feature
-- Date: 2024-02-01

BEGIN;

-- Add your schema changes here
ALTER TABLE stocks ADD COLUMN new_field VARCHAR(100);

COMMIT;
```

### Run Migrations

```bash
psql -U vnstock_user -d vnstock_db -f migrations/002_add_new_feature.sql
```

## 📈 Performance Optimization

### Indexes

The schema includes optimized indexes for:
- Stock symbol lookups
- Date range queries
- User-specific data
- Full-text search

### Partitioning (Optional)

For very large datasets (millions of rows), consider partitioning `stock_prices`:

```sql
-- Partition by year
CREATE TABLE stock_prices_2024 PARTITION OF stock_prices
FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
```

### Query Optimization Tips

1. **Use Views:** Pre-defined views like `latest_stock_prices`
2. **Index Usage:** Queries are optimized to use existing indexes
3. **Batch Inserts:** Use `COPY` or bulk inserts for large data loads
4. **Connection Pooling:** Use connection pools in application code

## 🛠️ Maintenance

### Vacuum and Analyze

```bash
# Run regularly to maintain performance
psql -U vnstock_user -d vnstock_db -c "VACUUM ANALYZE;"
```

### Check Database Size

```sql
SELECT pg_size_pretty(pg_database_size('vnstock_db'));
```

### Monitor Active Connections

```sql
SELECT count(*) FROM pg_stat_activity WHERE datname = 'vnstock_db';
```

## 📦 Backup and Restore

### Backup

```bash
# Full backup
pg_dump -U vnstock_user -F c vnstock_db > vnstock_backup.dump

# SQL format
pg_dump -U vnstock_user vnstock_db > vnstock_backup.sql
```

### Restore

```bash
# From custom format
pg_restore -U vnstock_user -d vnstock_db vnstock_backup.dump

# From SQL
psql -U vnstock_user -d vnstock_db < vnstock_backup.sql
```

## 🐛 Troubleshooting

### Connection Refused

```bash
# Check if PostgreSQL is running
docker-compose ps
# or
brew services list | grep postgresql
```

### Permission Denied

```bash
# Grant permissions
GRANT ALL PRIVILEGES ON DATABASE vnstock_db TO vnstock_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO vnstock_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO vnstock_user;
```

### Reset Database

```bash
# Drop and recreate
docker-compose down -v
docker-compose up -d
```

## 📚 Additional Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
- [node-postgres Documentation](https://node-postgres.com/)

## 🤝 Contributing

When adding new tables or modifying schema:

1. Create a migration file
2. Update this README
3. Update `queries.sql` with example queries
4. Test with seed data

## 📄 License

This database schema is part of the VNStock Analytics project.
