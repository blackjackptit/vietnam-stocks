# Investment Plans - Database Setup

Investment plans are now saved to the PostgreSQL database instead of browser localStorage, providing:
- Persistent storage across devices
- Better data integrity
- Historical price tracking for accurate performance comparison
- Session-based plan management

## Database Schema

### Tables Created

1. **investment_plans** - Stores plan metadata
   - plan_id (UUID)
   - name, notes, strategy information
   - budget, expected_return, risk_level, sharpe_ratio
   - session_id for user tracking
   - timestamps

2. **investment_plan_holdings** - Stores individual stock holdings
   - symbol, shares, buy_price
   - **price_at_creation** - Price when plan was created (for comparison)
   - allocation_percent, amount, expected_return

## Setup Instructions

### 1. Run the Database Migration

Make sure PostgreSQL is running:
```bash
cd database
docker compose up -d
```

Run the migration:
```bash
# Option 1: Using the helper script
./run_migration.sh

# Option 2: Manually with docker
docker compose exec postgres psql -U postgres -d vnstock < migrations/004_add_investment_plans.sql
```

### 2. Restart the API Server

```bash
# From project root
python api_server.py
```

The API server will automatically include the new endpoints:
- `GET /api/investment-plans` - Get all saved plans
- `POST /api/investment-plans` - Save a new plan
- `DELETE /api/investment-plans/<plan_id>` - Delete a plan

## Features

### 1. Save Plans with Current Prices
When you save an investment plan, the system captures:
- Your buy prices (from the plan)
- **Current market prices at the moment of saving**

This allows accurate comparison showing:
- How prices have changed since you created the plan
- Real performance vs. expected performance

### 2. Performance Tracking Metrics

Each saved plan displays:
- **Primary Metrics**: Initial investment, current value, profit/loss, annualized return
- **Comparison**: Expected return vs actual performance, performance status
- **Stock Analysis**: Best/worst performers
- **Advanced Analytics**: Win rate, average gain, total ROI, risk level, holdings count, Sharpe ratio

### 3. Historical Comparison
The "View Details" button shows:
- Buy price vs Current price for each stock
- Price change in VND and percentage
- Individual stock profit/loss

## API Endpoints

### GET /api/investment-plans
Returns all investment plans for the current session.

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "name": "Growth Portfolio Q1 2024",
      "notes": "Focus on tech stocks",
      "strategy": "growth",
      "strategyName": "High Growth Strategy",
      "budget": 100000000,
      "expectedReturn": 15.5,
      "risk": 12.3,
      "sharpeRatio": 1.26,
      "createdDate": "2024-02-05T10:30:00Z",
      "holdings": [
        {
          "symbol": "VCB",
          "shares": 100,
          "buyPrice": 95000,
          "priceAtCreation": 96000,
          "allocation": 20,
          "amount": 9500000,
          "expectedReturn": 18
        }
      ]
    }
  ],
  "count": 1
}
```

### POST /api/investment-plans
Save a new investment plan.

**Request Body:**
```json
{
  "name": "Growth Portfolio Q1 2024",
  "notes": "Focus on tech stocks",
  "strategy": "growth",
  "strategyName": "High Growth Strategy",
  "budget": 100000000,
  "expectedReturn": 15.5,
  "risk": 12.3,
  "sharpeRatio": 1.26,
  "holdings": [
    {
      "symbol": "VCB",
      "shares": 100,
      "buyPrice": 95000,
      "priceAtCreation": 96000,
      "allocation": 20,
      "amount": 9500000,
      "expectedReturn": 18
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "planId": "uuid",
  "message": "Investment plan saved successfully"
}
```

### DELETE /api/investment-plans/{plan_id}
Delete an investment plan.

**Response:**
```json
{
  "success": true,
  "message": "Investment plan deleted successfully"
}
```

## Migration from localStorage

If you had plans saved in localStorage, they will need to be re-created in the new system. The old localStorage data is not automatically migrated to preserve data integrity and ensure all plans have accurate price_at_creation values.

## Troubleshooting

### Migration Fails
```bash
# Check if PostgreSQL is running
docker compose ps

# View logs
docker compose logs postgres

# Connect to database manually
docker compose exec postgres psql -U postgres -d vnstock

# Check if tables exist
\dt investment*
```

### API Errors
Check the API server logs for detailed error messages:
```bash
python api_server.py
```

### No Plans Showing
1. Check browser console for API errors
2. Verify session cookies are enabled
3. Check network tab in browser DevTools for API response

## Benefits Over localStorage

1. **Persistent Storage** - Plans survive browser data clearing
2. **Historical Tracking** - Accurate price-at-creation recording
3. **Multi-Device Access** - Session-based access from any device
4. **Better Performance** - Database indexing for fast queries
5. **Data Integrity** - Relational database constraints
6. **Backup & Recovery** - Database backup includes all plans
