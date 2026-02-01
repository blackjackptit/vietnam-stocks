# 📅 Automated Data Collection Jobs

This directory contains automated jobs for collecting stock and macro economic data.

## 📋 Contents

- `collect_stock_data.py` - Collects stock prices and updates database
- `collect_macro_data.py` - Collects market indices and economic indicators
- `scheduler.py` - Manages scheduled execution of jobs
- `start_scheduler.sh` - Shell script to start the scheduler
- `com.vnstock.scheduler.plist` - macOS LaunchAgent configuration

## ⏰ Schedule

### Stock Data Collection
- **Hourly during market hours**: Mon-Fri, 9:05 AM - 3:05 PM
- **End of day update**: Mon-Fri, 3:30 PM
- Collects: Current prices, volume, change %

### Macro Data Collection
- **Daily**: Every day at 6:00 AM
- **Half-hourly during market hours**: Mon-Fri, 9:00 AM - 3:30 PM (every 30 min)
- Collects: VN-Index, HNX-Index, UPCOM-Index, USD/VND rate

## 🚀 Quick Start

### Install Dependencies

```bash
cd /Users/nghia.dinh/Projects/vietnam-stocks
source venv/bin/activate
pip install -r requirements.txt
```

### Test Jobs Manually

```bash
# Test stock data collection
python jobs/collect_stock_data.py

# Test macro data collection
python jobs/collect_macro_data.py

# Test scheduler (run all jobs once)
python jobs/scheduler.py --now

# Test stock collection only
python jobs/scheduler.py --stock-only

# Test macro collection only
python jobs/scheduler.py --macro-only
```

### Start Scheduler (Interactive Mode)

```bash
# Run scheduler in foreground (Ctrl+C to stop)
python jobs/scheduler.py
```

## 🔧 Setup Automatic Scheduling (macOS)

### Option 1: Using Launchd (Recommended for macOS)

1. **Make scripts executable**:
```bash
chmod +x jobs/start_scheduler.sh
```

2. **Copy plist to LaunchAgents**:
```bash
cp jobs/com.vnstock.scheduler.plist ~/Library/LaunchAgents/
```

3. **Load the service**:
```bash
launchctl load ~/Library/LaunchAgents/com.vnstock.scheduler.plist
```

4. **Start the service**:
```bash
launchctl start com.vnstock.scheduler
```

### Manage the Service

```bash
# Check if running
launchctl list | grep vnstock

# Stop the service
launchctl stop com.vnstock.scheduler

# Unload the service (disable automatic start)
launchctl unload ~/Library/LaunchAgents/com.vnstock.scheduler.plist

# View logs
tail -f /tmp/vnstock_scheduler.out.log
tail -f /tmp/vnstock_scheduler.err.log
tail -f /tmp/stock_scheduler.log
```

### Option 2: Using screen/tmux (Alternative)

```bash
# Start in a detached screen session
screen -dmS vnstock-scheduler bash -c "cd /Users/nghia.dinh/Projects/vietnam-stocks && source venv/bin/activate && python jobs/scheduler.py"

# Attach to the session
screen -r vnstock-scheduler

# Detach: Ctrl+A, then D
```

### Option 3: Using nohup (Simple Background Process)

```bash
cd /Users/nghia.dinh/Projects/vietnam-stocks
source venv/bin/activate
nohup python jobs/scheduler.py > /tmp/scheduler.log 2>&1 &

# Check if running
ps aux | grep scheduler.py

# Stop
pkill -f scheduler.py
```

## 📊 What Data is Collected

### Stock Data (`collect_stock_data.py`)
- **Source**: VNDirect API
- **Data**: Open, High, Low, Close, Volume, Change, Change %
- **Storage**: `stock_prices` table in PostgreSQL
- **Update**: Hourly during market hours, plus end-of-day

### Market Indices (`collect_macro_data.py`)
- **VN-Index**: HOSE main index
- **HNX-Index**: Hanoi Stock Exchange index
- **UPCOM-Index**: Unlisted Public Company Market index
- **Storage**: `market_indices` table

### Macro Indicators (`collect_macro_data.py`)
- **USD/VND Exchange Rate**: From Vietcombank
- **Storage**: `macro_indicators` table

## 🔍 Monitoring

### Check Logs

```bash
# Scheduler log
tail -f /tmp/stock_scheduler.log

# LaunchAgent output logs
tail -f /tmp/vnstock_scheduler.out.log
tail -f /tmp/vnstock_scheduler.err.log
```

### View Next Scheduled Jobs

```bash
# When scheduler is running interactively
# Press Ctrl+C to see job schedule
```

### Database Verification

```bash
# Check latest stock prices
psql -U vnstock_user -d vnstock_db -c "SELECT symbol, date, close, volume FROM stock_prices ORDER BY date DESC LIMIT 10;"

# Check market indices
psql -U vnstock_user -d vnstock_db -c "SELECT index_code, date, value, change_percent FROM market_indices ORDER BY date DESC LIMIT 5;"

# Check macro indicators
psql -U vnstock_user -d vnstock_db -c "SELECT indicator_name, date, value FROM macro_indicators ORDER BY date DESC LIMIT 5;"
```

## ⚙️ Configuration

### Change Schedule

Edit `jobs/scheduler.py` and modify the `setup_jobs()` method:

```python
# Example: Change stock collection to every 2 hours
self.scheduler.add_job(
    self.collect_stocks,
    CronTrigger(
        day_of_week='mon-fri',
        hour='9-15/2',  # Every 2 hours
        minute=5
    ),
    ...
)
```

### Add More Data Sources

1. Create a new method in `MacroDataCollector` class
2. Call it from the `collect_macro_indicators()` method
3. Save results using `save_indicators_to_database()`

## 🐛 Troubleshooting

### Scheduler not starting

```bash
# Check Python path
which python

# Check virtual environment
source venv/bin/activate
python --version

# Check dependencies
pip list | grep APScheduler
```

### Jobs not running

```bash
# Check scheduler is running
ps aux | grep scheduler.py

# Check logs for errors
tail -50 /tmp/stock_scheduler.log

# Test job manually
python jobs/collect_stock_data.py
```

### Database connection errors

```bash
# Test database connection
python database/test_connection.py

# Check PostgreSQL is running
docker ps | grep postgres

# Restart PostgreSQL if needed
cd database && docker compose restart
```

### API errors

- **VNDirect API**: May have rate limits, scheduler includes delays
- **Network issues**: Jobs will retry on next schedule
- **No data**: Check if market is open

## 📈 Performance

- **Stock collection**: ~30 seconds for 31 stocks
- **Macro collection**: ~5 seconds for all indices
- **Database impact**: Minimal (uses ON CONFLICT for upserts)
- **API calls**: ~1 per stock per hour during market hours

## 🔐 Security

- Database credentials stored in `.env` file
- API calls use standard HTTPS
- No sensitive data in logs
- Runs as user process (not root)

## 📝 Notes

- Vietnamese stock market hours: 9:00 AM - 3:00 PM (Mon-Fri)
- Market closed on public holidays
- Some APIs may have rate limits
- Gold/Oil prices require additional API integration

## 🆘 Support

For issues or questions:
1. Check logs: `/tmp/stock_scheduler.log`
2. Test manually: `python jobs/scheduler.py --now`
3. Verify database: Run test queries above
4. Check API status: Test VNDirect API manually

## 📚 References

- [APScheduler Documentation](https://apscheduler.readthedocs.io/)
- [VNDirect API](https://finfo-api.vndirect.com.vn/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
