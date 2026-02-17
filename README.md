# Vietnamese Stock Analytics Platform

A comprehensive, bilingual (Vietnamese/English) stock analysis and trading platform for the Vietnamese stock market.

## 🌟 Features

- **Real-time Stock Monitoring** - Track 31+ Vietnamese stocks with live price updates
- **Technical Analysis** - RSI, MACD, Moving Averages, and custom scoring system
- **Price Forecasting** - ML-powered price predictions
- **Trading Automation** - Automated trading with risk management
- **Macro Analysis** - Economic indicators and geopolitical factors
- **Portfolio Tracking** - Watchlist management and performance tracking
- **Bilingual Interface** - Full Vietnamese and English language support
- **Advanced Charts** - Interactive visualizations with Chart.js

## 🐳 Docker Deployment

This project includes complete Docker support for easy deployment:

- **Dockerfile** - Optimized Python 3.11 image
- **docker-compose.yml** - Multi-service orchestration
- **docker-compose.dev.yml** - Development with live reload
- **Makefile** - Convenient command shortcuts

Quick commands using Makefile:
```bash
make setup      # Initial environment setup
make up         # Start all services
make logs       # View logs
make db-init    # Initialize database
make status     # Check service health
make down       # Stop services
```

For detailed Docker documentation, see [DOCKER_SETUP.md](DOCKER_SETUP.md).

## 📁 Project Structure

```
vn-stock-analytics/
├── app/                    # Application files
│   ├── pages/             # HTML application pages (15 files)
│   │   ├── index.html              # Homepage
│   │   ├── dashboard.html          # Main dashboard
│   │   ├── dashboard_advanced.html # Advanced features
│   │   ├── dashboard_history.html  # Historical analysis
│   │   ├── price_forecast.html     # ML price predictions
│   │   ├── trading_automation.html # Automated trading
│   │   ├── macro_analysis.html     # Macro indicators
│   │   ├── advanced_charts.html    # Technical charts
│   │   ├── alerts_system.html      # Price alerts
│   │   └── settings.html           # User settings
│   └── static/            # Static assets
│       ├── css/           # Stylesheets
│       │   └── theme.css
│       └── js/            # JavaScript modules
│           └── i18n.js    # Internationalization
│
├── src/                   # Core Python modules
│   ├── technical_analysis.py
│   ├── portfolio.py
│   ├── demo_data.py
│   └── realtime_server.py
│
├── jobs/                  # Scheduled data collection jobs
│   ├── scheduler.py           # Job scheduler
│   ├── collect_stock_data.py  # Stock data collector
│   └── collect_macro_data.py  # Macro data collector
│
├── scripts/               # Utility scripts
│   ├── data/             # Data fetching and generation
│   │   ├── fetch_vnstock.py
│   │   ├── fetch_real_data.py
│   │   ├── generate_all_data.py
│   │   └── sync_data_to_db.py
│   ├── translations/     # i18n and localization
│   │   ├── add_i18n_to_pages.py
│   │   └── check_translations.py
│   ├── database/         # Database utilities
│   │   └── api_server_db.py
│   ├── utils/            # General utilities
│   │   ├── convert_md_to_html.py
│   │   └── fix_api_urls.py
│   ├── demo_monitor.py        # Demo monitoring
│   ├── monitor.py             # Production monitoring
│   ├── serve_dashboard.py     # Simple HTTP server
│   └── realtime_server.py     # SSE real-time server
│
├── docs/                  # Documentation
│   ├── guides/           # User guides
│   │   ├── AUTOMATED_TRADING_GUIDE.md
│   │   ├── HISTORICAL_ANALYSIS_GUIDE.md
│   │   ├── WATCHLIST_GUIDE.md
│   │   └── QUICKSTART.md
│   ├── api/              # API documentation
│   │   ├── API_ENDPOINTS.md
│   │   ├── API_SERVER_SETUP.md
│   │   └── CONFIG_README.md
│   └── development/      # Development docs
│       ├── FEATURES_COMPLETE.md
│       └── IMPLEMENTATION_COMPLETE.md
│
├── database/              # Database setup and migrations
│   ├── schema.sql
│   └── seed_data.sql
│
├── data/                  # Data files
│   └── (JSON data files)
│
├── logs/                  # Log files
│   └── (Application logs)
│
├── output/                # Generated outputs
│   └── (Scan results, reports)
│
├── tests/                 # Test files
│   ├── test_backtest.html
│   ├── test_charts.html
│   └── test_language.html
│
├── api_server.py          # Main Flask API server
├── config.py              # Configuration settings
├── run.py                 # Application entry point
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Docker services orchestration
├── docker-compose.dev.yml # Development overrides
├── docker-entrypoint.sh   # Container startup script
├── Makefile               # Docker command shortcuts
├── .env                   # Environment variables (not in git)
├── .env.example           # Environment template (manual)
├── .env.docker            # Environment template (Docker)
├── .dockerignore          # Docker build exclusions
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── DOCKER_SETUP.md        # Complete Docker guide
```

## 🚀 Quick Start

### Option 1: Docker (Recommended) 🐳

**Prerequisites**: Docker 20.10+ and Docker Compose 2.0+

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd vn-stock-analytics
   ```

2. **Configure environment**
   ```bash
   cp .env.docker .env
   # Edit .env and update passwords/secrets
   ```

3. **Start all services**
   ```bash
   docker compose up -d
   ```

4. **Initialize database** (first time only)
   ```bash
   docker compose exec app python scripts/data/sync_data_to_db.py
   ```

5. **Access the application**
   - Web Interface: http://localhost:5000
   - API Health: http://localhost:5000/health
   - PgAdmin: http://localhost:5050 (optional)

**Useful commands:**
```bash
docker compose logs -f              # View logs
docker compose ps                   # Check status
docker compose down                 # Stop services
docker compose restart              # Restart services
```

See [DOCKER_SETUP.md](DOCKER_SETUP.md) for complete Docker documentation.

### Option 2: Manual Installation

**Prerequisites**: Python 3.11+, PostgreSQL 15+

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd vn-stock-analytics
   ```

2. **Set up Python environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Start PostgreSQL database**
   ```bash
   cd database
   docker compose up -d
   cd ..
   ```

5. **Initialize database**
   ```bash
   python scripts/data/sync_data_to_db.py
   ```

6. **Start the application**
   ```bash
   # Start API server
   python api_server.py

   # In another terminal, start scheduler
   source venv/bin/activate
   python jobs/scheduler.py
   ```

7. **Access the application**
   - Open browser: http://localhost:5000
   - Homepage with navigation to all features

## 📖 Usage Guide

### Main Dashboard
- View real-time stock prices, changes, and technical indicators
- Interactive heatmap organized by sectors
- Score distribution and RSI analysis
- Watchlist management

### Price Forecasting
- Machine learning-based price predictions
- Multiple forecasting periods (7, 14, 30 days)
- Visual charts and confidence intervals

### Trading Automation
- Configure broker API connections
- Set up automated trading rules
- Risk management controls
- Backtesting capabilities

### Macro Analysis
- Economic indicators (GDP, inflation, interest rates)
- Currency and commodity trends
- Geopolitical risk assessment
- Policy impact timeline

## 🔧 Configuration

Edit `.env` file to configure:

```bash
# API Server
API_HOST=0.0.0.0
API_PORT=5000
API_DEBUG=false

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=vnstocks
DB_USER=postgres
DB_PASSWORD=your_password

# Data Collection
AUTO_COLLECT_ENABLED=true
STOCK_COLLECTION_INTERVAL=3600  # 1 hour
MACRO_COLLECTION_INTERVAL=86400 # 24 hours

# Market Hours
MARKET_OPEN_HOUR=9
MARKET_CLOSE_HOUR=15
MARKET_DAYS=mon-fri
```

See `docs/api/CONFIG_README.md` for full configuration options.

## 🌐 API Endpoints

### Stock Data
- `GET /api/stocks` - Get all stocks
- `GET /api/stock/:symbol` - Get stock by symbol
- `GET /api/stock/:symbol/current` - Get current price
- `GET /api/stock/:symbol/history?days=30` - Get historical prices
- `GET /api/latest` - Get latest data for all stocks
- `GET /api/top-gainers?limit=10` - Get top gainers
- `GET /api/top-losers?limit=10` - Get top losers

### Market Data
- `GET /api/indices` - Get market indices
- `GET /api/search?q=query` - Search stocks

### System
- `GET /health` - Health check
- `GET /api/system-status` - System status
- `GET /api/controls` - Get system controls

See `docs/api/API_ENDPOINTS.md` for complete API documentation.

## 📊 Data Collection

The platform collects data from multiple sources:

1. **vnstock** - Vietnamese stock market data library
2. **SSI iBoard** - Ho Chi Minh Stock Exchange data
3. **Manual imports** - Custom data sources

### Scheduled Jobs

Jobs are configured in `config.py` and run via `jobs/scheduler.py`:

- **Stock prices** - Every 1 hour during market hours
- **Market indices** - Every 30 minutes
- **Macro indicators** - Daily at 6:00 AM
- **End of day** - 15:30 on trading days

## 🧪 Testing

Run tests:
```bash
# Open test pages in browser
open tests/test_charts.html
open tests/test_language.html
open tests/test_backtest.html
```

## 🌍 Internationalization

The platform supports Vietnamese and English:

- Toggle language using the selector in the top navigation
- Translations stored in `app/static/js/i18n.js`
- All pages support both languages
- Alert messages and system notifications translated

## 🔐 Security Notes

- Never commit `.env` file to git
- Use environment variables for sensitive data
- API server includes CORS configuration
- Database credentials should be rotated regularly
- Use SSL/TLS in production environments

## 📝 Development

### Adding New Features

1. Create HTML page in `app/pages/`
2. Add translations to `app/static/js/i18n.js`
3. Update navigation menu in existing pages
4. Document in `docs/guides/`

### Database Schema Updates

1. Update `database/schema.sql`
2. Create migration script in `scripts/database/`
3. Test with development database
4. Document changes in `docs/api/`

### Contributing

See development documentation in `docs/development/` for:
- Code style guidelines
- Testing procedures
- Pull request process

## 🐛 Troubleshooting

### Common Issues

1. **Database connection failed**
   ```bash
   cd database && docker compose up -d
   ```

2. **Scheduler not running**
   ```bash
   ps aux | grep scheduler.py
   python jobs/scheduler.py
   ```

3. **Empty charts/no data**
   ```bash
   python scripts/data/sync_data_to_db.py
   ```

4. **Translation not working**
   - Check browser console for errors
   - Verify `app/static/js/i18n.js` is loaded
   - Clear browser cache

## 📜 License

[Add your license here]

## 👥 Authors

[Add author information]

## 🙏 Acknowledgments

- **vnstock** - Vietnamese stock data library
- **Chart.js** - Interactive charts
- **Flask** - Web framework
- **PostgreSQL** - Database

## 📞 Support

For issues and questions:
- GitHub Issues: [repository-url]/issues
- Documentation: `docs/` directory
- Quick Start: `docs/guides/QUICKSTART.md`

---

**Built with ❤️ for Vietnamese stock traders**
