# Docker Setup Guide - Vietnamese Stock Analytics Platform

Complete guide for running Vietnamese Stock Analytics Platform with Docker.

## 📦 What's Included

This project has been fully dockerized with production-ready configuration:

### Docker Files
- **Dockerfile** - Optimized Python 3.11 image with health checks
- **docker-compose.yml** - Multi-service orchestration
- **docker-compose.dev.yml** - Development overrides with live reload
- **.dockerignore** - Build optimization
- **.env.docker** - Environment configuration template
- **docker-entrypoint.sh** - Startup script with health checks
- **Makefile** - 20+ convenient command shortcuts
- **.github/workflows/docker-build.yml** - CI/CD pipeline

### Services Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Docker Network                          │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Flask API  │  │  Scheduler   │  │  PostgreSQL  │    │
│  │  (port 5000) │  │  (background)│  │  (port 5432) │    │
│  │              │  │              │  │              │    │
│  │  - REST API  │  │  - Jobs      │  │  - Database  │    │
│  │  - Web UI    │  │  - Cron      │  │  - Volumes   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
│         │                  │                  │           │
│         └──────────────────┴──────────────────┘           │
│                                                             │
│  ┌──────────────┐                                          │
│  │   PgAdmin    │  (Optional)                             │
│  │  (port 5050) │                                          │
│  └──────────────┘                                          │
└─────────────────────────────────────────────────────────────┘
           │                    │
    Host Port 5000      Host Port 5432
```

### Before Docker vs After Docker

**Before (Manual Setup):**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd database && docker compose up -d && cd ..
python api_server.py
# In another terminal
python jobs/scheduler.py
```

**After (Docker Setup):**
```bash
docker compose up -d
```

That's it! All services start automatically with proper dependencies.

## 📋 Prerequisites

- Docker 20.10+ ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose 2.0+ (included with Docker Desktop)
- 2GB+ available RAM
- 5GB+ available disk space

## 🚀 Quick Start

### 1. Configure Environment

Copy the Docker environment template:

```bash
cp .env.docker .env
```

Edit `.env` and update the following values:

```bash
# IMPORTANT: Change these in production!
DB_PASSWORD=your_secure_database_password
JWT_SECRET=your_random_jwt_secret_key
SESSION_SECRET=your_random_session_secret
PGADMIN_PASSWORD=your_pgadmin_password
```

**Quick way to generate secure secrets:**
```bash
openssl rand -hex 32
```

### 2. Start the Application

Start all services:

```bash
docker compose up -d
```

This will start:
- **PostgreSQL** database (port 5432)
- **Flask API** server (port 5000)
- **Scheduler** for background jobs

### 3. Initialize Database (First Time Only)

After first startup, initialize the database with stock data:

```bash
docker compose exec app python scripts/data/sync_data_to_db.py
```

### 4. Access the Application

- **Web Interface**: http://localhost:5000
- **API Health**: http://localhost:5000/health
- **API Documentation**: http://localhost:5000/api/stocks

### 5. View Logs

```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f app
docker compose logs -f scheduler
docker compose logs -f postgres
```

## 🛠️ Using Makefile (Recommended)

The included Makefile provides convenient shortcuts for all Docker operations.

### Setup and Start
```bash
make setup          # Copy .env.docker to .env
make build          # Build Docker images
make up             # Start all services
make status         # Check service status
make health         # Check application health
```

### Monitoring
```bash
make logs           # View all logs
make logs-app       # View app logs only
make logs-scheduler # View scheduler logs only
make logs-db        # View database logs only
```

### Database Operations
```bash
make db-init        # Initialize database with data
make db-shell       # Open PostgreSQL shell
make db-backup      # Backup database to backups/
make db-restore FILE=backups/file.sql  # Restore from backup
make db-reset       # Reset database (WARNING: deletes data)
```

### Container Operations
```bash
make shell          # Open bash shell in app container
make restart        # Restart all services
make down           # Stop all services
make clean          # Remove containers
make clean-all      # Remove containers, volumes, images
```

### Development
```bash
make dev            # Start in development mode with live reload
make test           # Run tests in container
```

### Complete Command List
```bash
make help           # Show all available commands
```

## 🔧 Development Mode

For development with live code reloading:

```bash
# Method 1: Using Makefile
make dev

# Method 2: Using docker compose
docker compose -f docker-compose.yml -f docker-compose.dev.yml up
```

Development mode features:
- Source code mounted as volumes (live reload)
- Debug mode enabled
- Verbose logging
- PgAdmin UI enabled by default

## 📊 Optional: PgAdmin Database UI

To enable PgAdmin for database management:

```bash
# Start with tools profile
docker compose --profile tools up -d

# Or add to existing services
docker compose up -d pgadmin
```

Access PgAdmin at http://localhost:5050:
- Email: `admin@vnstock.com` (from .env)
- Password: `admin123` (from .env)

**Connect to database in PgAdmin:**
- Host: `postgres`
- Port: `5432`
- Database: `vnstock_db`
- Username: `vnstock_user`
- Password: (from your .env)

## 🔧 Common Commands

### Start Services

```bash
# Start all services in background
docker compose up -d

# Start specific service
docker compose up -d app

# Start without scheduler
docker compose up -d postgres app

# Start with output visible (foreground)
docker compose up
```

### Stop Services

```bash
# Stop all services
docker compose down

# Stop and remove volumes (WARNING: deletes database data)
docker compose down -v

# Stop specific service
docker compose stop app
```

### Restart Services

```bash
# Restart all
docker compose restart

# Restart specific service
docker compose restart app
```

### View Status

```bash
# List running containers
docker compose ps

# Check health status
docker inspect vnstock_app | grep -A 5 Health

# View resource usage
docker stats
```

### Execute Commands in Container

```bash
# Open shell in app container
docker compose exec app bash

# Run Python script
docker compose exec app python scripts/data/fetch_vnstock.py

# Database commands
docker compose exec postgres psql -U vnstock_user -d vnstock_db

# Check Python packages
docker compose exec app pip list
```

### Build and Update

```bash
# Rebuild images
docker compose build

# Rebuild specific service
docker compose build app

# Rebuild without cache
docker compose build --no-cache

# Pull latest base images and rebuild
docker compose build --pull

# Rebuild and restart
docker compose up -d --build
```

## 📦 Volume Management

### Data Persistence

The following data persists across container restarts:

**Docker Volumes:**
- `postgres_data` - Database files
- `pgadmin_data` - PgAdmin settings

**Mounted Directories:**
- `./data` - Application data files
- `./output` - Generated outputs and reports
- `./logs` - Application and scheduler logs

### Backup Database

```bash
# Using Makefile (recommended)
make db-backup

# Manual backup to file
docker compose exec postgres pg_dump -U vnstock_user vnstock_db > backup.sql

# Backup with compression
docker compose exec postgres pg_dump -U vnstock_user vnstock_db | gzip > backup.sql.gz

# Backup with timestamp
docker compose exec postgres pg_dump -U vnstock_user vnstock_db > "backup_$(date +%Y%m%d_%H%M%S).sql"
```

### Restore Database

```bash
# Using Makefile
make db-restore FILE=backups/vnstock_backup_20260217_123456.sql

# Manual restore from file
docker compose exec -T postgres psql -U vnstock_user -d vnstock_db < backup.sql

# Restore from compressed file
gunzip -c backup.sql.gz | docker compose exec -T postgres psql -U vnstock_user -d vnstock_db
```

### Clear Data

```bash
# Stop services and remove volumes
docker compose down -v

# Remove specific volume
docker volume rm vn-stock-analytics_postgres_data

# Remove all unused volumes
docker volume prune
```

## 🔍 Troubleshooting

### Docker Desktop Not Running

```bash
# Check if Docker is running
docker version

# Error: "Cannot connect to Docker daemon"
# Solution: Start Docker Desktop (Windows/Mac) or Docker daemon (Linux)
# Windows/Mac: Open Docker Desktop application
# Linux: sudo systemctl start docker
```

### Database Connection Failed

```bash
# Check if postgres is running
docker compose ps postgres

# Check postgres logs
docker compose logs postgres

# Check connection from app
docker compose exec app python -c "from config import get_database_connection; get_database_connection()"

# Restart postgres
docker compose restart postgres
```

### Application Won't Start

```bash
# Check app logs
docker compose logs app

# Check health status
docker compose ps app

# Check if database is ready
docker compose exec postgres pg_isready -U vnstock_user

# Rebuild image
docker compose build app
docker compose up -d app

# Check for errors in entrypoint
docker compose logs app --tail 50
```

### Out of Memory

```bash
# Check resource usage
docker stats

# Increase Docker memory limit
# Docker Desktop > Settings > Resources > Memory
# Recommended: 4GB+ for full stack

# Check container memory limits
docker inspect vnstock_app | grep -i memory
```

### Port Already in Use

```bash
# Check what's using the port
# Windows
netstat -ano | findstr :5000

# Linux/Mac
lsof -i :5000

# Solution 1: Stop the conflicting service
# Solution 2: Change port in .env
API_PORT=5001
docker compose up -d
```

### Containers Keep Restarting

```bash
# Check container logs
docker compose logs app

# Common issues:
# 1. Database not ready - wait 10-20 seconds
# 2. Missing dependencies - rebuild image
# 3. Configuration error - check .env file
# 4. Port conflict - change ports

# Force stop and restart
docker compose down
docker compose up -d
```

### Database Reset

```bash
# Using Makefile (with confirmation)
make db-reset

# Manual method
docker compose down
docker volume rm vn-stock-analytics_postgres_data
docker compose up -d
sleep 10
docker compose exec app python scripts/data/sync_data_to_db.py
```

### Permission Issues (Linux)

```bash
# Fix file permissions
sudo chown -R $USER:$USER ./data ./output ./logs

# Run Docker without sudo
sudo usermod -aG docker $USER
# Log out and back in
```

### Image Build Fails

```bash
# Check Docker space
docker system df

# Clean up unused resources
docker system prune -a

# Rebuild without cache
docker compose build --no-cache

# Check Dockerfile syntax
docker compose config
```

## 🌐 Production Deployment

### Security Checklist

Before deploying to production:

- [ ] Change all default passwords in `.env`
- [ ] Generate secure random secrets (use `openssl rand -hex 32`)
- [ ] Use strong database password (32+ characters)
- [ ] Disable DEBUG mode (`DEBUG=false`)
- [ ] Set NODE_ENV to `production`
- [ ] Configure firewall rules (close unnecessary ports)
- [ ] Use HTTPS/SSL (nginx reverse proxy recommended)
- [ ] Set up regular database backups
- [ ] Configure log rotation
- [ ] Monitor logs and health checks
- [ ] Update CORS_ORIGINS in config.py
- [ ] Set resource limits in docker-compose.yml
- [ ] Use Docker secrets for sensitive data
- [ ] Enable firewall on host
- [ ] Set up monitoring (Prometheus, Grafana)

### Required Environment Variables

```bash
NODE_ENV=production
DEBUG=false
DB_PASSWORD=<secure-password-32-chars>
JWT_SECRET=<random-secret-64-chars>
SESSION_SECRET=<random-secret-64-chars>
```

### Nginx Reverse Proxy (Recommended)

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    ssl_certificate /etc/ssl/certs/yourdomain.crt;
    ssl_certificate_key /etc/ssl/private/yourdomain.key;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

### Resource Limits (Production)

Add to docker-compose.yml:

```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
```

### Recommended Resources

Minimum for production:
- **CPU**: 2 cores
- **RAM**: 4GB
- **Disk**: 20GB SSD
- **Network**: 10 Mbps

Recommended for high traffic:
- **CPU**: 4 cores
- **RAM**: 8GB
- **Disk**: 50GB SSD
- **Network**: 100 Mbps

## 📈 Monitoring and Health Checks

### Health Check Endpoints

```bash
# Application health
curl http://localhost:5000/health

# Expected response:
# {"status": "healthy", "database": "connected", "timestamp": "..."}

# Database health
docker compose exec postgres pg_isready -U vnstock_user

# Check all container health
docker compose ps
```

### Built-in Health Checks

All services include health checks:

- **PostgreSQL**: `pg_isready` every 10s
- **Flask API**: `GET /health` every 30s
- **Docker**: Automatic container health monitoring

### Log Monitoring

```bash
# Real-time logs
make logs

# Application logs (in host)
tail -f logs/api_server.log

# Scheduler logs
tail -f logs/scheduler.log

# Search logs for errors
docker compose logs | grep -i error

# Export logs
docker compose logs > all_logs.txt
```

### Automated Monitoring Setup

```bash
# Install monitoring stack (optional)
# Prometheus + Grafana for metrics
# ELK stack for log aggregation
# Alert manager for notifications
```

## 🔄 Updates and Maintenance

### Update Application Code

```bash
# Pull latest code
git pull origin main

# Rebuild and restart
make rebuild

# Or manually
docker compose build --pull
docker compose up -d

# Check if update successful
make logs
make health
```

### Update Dependencies

```bash
# Update requirements.txt
# Then rebuild
docker compose build --no-cache app
docker compose up -d app
```

### Database Migrations

```bash
# Run migration script
docker compose exec app python scripts/database/migrate.py

# Verify migration
docker compose exec app python scripts/database/verify.py
```

### Scheduled Maintenance

```bash
# Weekly backup
0 2 * * 0 make db-backup

# Monthly cleanup
0 3 1 * * docker system prune -af

# Daily health check
0 * * * * make health || notify-admin
```

## 🧪 Testing

### Run Tests

```bash
# Run all tests
make test

# Run specific test
docker compose exec app python -m pytest tests/test_specific.py

# Run with coverage
docker compose exec app python -m pytest --cov=. --cov-report=html

# Interactive testing
docker compose exec app python
>>> from src import technical_analysis
>>> # Test interactively
```

### Integration Testing

```bash
# Test database connection
docker compose exec app python -c "from config import get_database_connection; conn = get_database_connection(); print('✓ Connected')"

# Test API endpoint
curl -f http://localhost:5000/health && echo "✓ API healthy"

# Test data collection
docker compose exec app python scripts/data/fetch_vnstock.py
```

## 📞 Support and Resources

### Documentation
- **This file** - Complete Docker setup guide
- **README.md** - Application overview and features
- **docs/** - Feature-specific guides
- **Makefile** - Run `make help` for all commands

### Getting Help

1. **Check logs**: `docker compose logs`
2. **Verify configuration**: Review `.env` file
3. **Check health**: `docker compose ps`
4. **Review documentation**: This file and README.md
5. **GitHub Issues**: Report bugs or request features

### Common Issues
- Port conflicts → Change ports in `.env`
- Memory issues → Increase Docker memory limit
- Database errors → Check postgres logs
- Build failures → Run `docker system prune -a` and rebuild

## 🗑️ Complete Cleanup

To completely remove all Docker resources:

```bash
# Using Makefile (with confirmation)
make clean-all

# Manual cleanup
# Stop and remove containers
docker compose down

# Remove volumes (deletes all data)
docker compose down -v

# Remove images
docker rmi $(docker images 'vn-stock-analytics*' -q)

# Remove all unused resources
docker system prune -a --volumes

# Remove everything
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
docker volume rm $(docker volume ls -q)
docker network prune -f
```

## 🎯 Best Practices

### Development
- Use `make dev` for local development
- Keep source code on host, use volumes
- Commit `.env.docker` but not `.env`
- Use `.dockerignore` to exclude files
- Regularly pull latest changes

### Production
- Use specific image tags, not `latest`
- Set resource limits
- Use health checks
- Enable automatic restart
- Regular backups
- Monitor logs and metrics
- Use secrets management
- Enable SSL/TLS
- Keep Docker updated

### Security
- Change all default passwords
- Use strong secrets (32+ chars)
- Don't expose unnecessary ports
- Keep images updated
- Scan for vulnerabilities
- Use non-root users
- Limit container privileges

## 📋 Quick Reference

```bash
# Essential Commands
make setup          # Initial setup
make up             # Start services
make down           # Stop services
make logs           # View logs
make status         # Check status
make db-init        # Initialize database

# Development
make dev            # Dev mode with live reload
make shell          # Open shell in container
make test           # Run tests

# Database
make db-backup      # Backup database
make db-shell       # PostgreSQL shell
make db-reset       # Reset database

# Maintenance
make rebuild        # Rebuild images
make clean          # Remove containers
make health         # Check health
```

---

**Built with 🐳 Docker for seamless deployment**

For application-specific documentation, see [README.md](README.md)
