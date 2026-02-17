# Vietnamese Stock Analytics - Production Deployment Checklist

Complete pre-deployment checklist to ensure a smooth and secure production launch.

---

## Pre-Deployment Checklist

### ✅ Security & Secrets

- [ ] **Validate Production Secrets**
  ```bash
  python scripts/validate_secrets.py
  ```
  - Ensure all default secrets are changed
  - JWT_SECRET minimum 32 characters
  - SESSION_SECRET minimum 32 characters
  - DB_PASSWORD minimum 12 characters

- [ ] **Update Environment Variables**
  - Copy `.env.example` to `.env`
  - Set `NODE_ENV=production`
  - Set `DEBUG=false`
  - Update database credentials
  - Configure CORS_ORIGINS for production domains

- [ ] **Secure Database**
  - Change PostgreSQL default password
  - Restrict database access to application servers only
  - Enable SSL/TLS for database connections
  - Set up database backups (automated daily)

- [ ] **API Security**
  - Review CORS allowed origins (no wildcards '*')
  - Enable HTTPS/TLS for API endpoints
  - Configure rate limiting (if needed)
  - Review exposed endpoints for sensitive data

---

### ✅ Configuration Validation

- [ ] **Run Configuration Tests**
  ```bash
  python config.py
  ```
  - Verify database connection
  - Check pool settings (min/max connections)
  - Validate API port configuration
  - Test environment variable loading

- [ ] **Database Pool Tuning**
  - Review pool settings for expected load:
    - Small (1-10 users): `DB_POOL_MAX=10-20`
    - Medium (10-50 users): `DB_POOL_MAX=20-50`
    - Large (50+ users): `DB_POOL_MAX=50-100`
  - Ensure `DB_POOL_MAX < PostgreSQL max_connections`

- [ ] **Log Configuration**
  - Verify log paths are writable
  - Set appropriate log levels (INFO or WARNING for production)
  - Configure log rotation (daily, keep 30 days)
  - Test error logging and monitoring

---

### ✅ Docker & Infrastructure

- [ ] **Build Docker Images**
  ```bash
  docker compose build
  ```
  - Verify build succeeds without errors
  - Check image sizes (should be reasonable)
  - Test multi-stage builds work correctly

- [ ] **Test Docker Compose**
  ```bash
  docker compose up -d
  docker compose ps
  docker compose logs
  ```
  - All services start successfully
  - Health checks pass (postgres, app, scheduler)
  - No error messages in logs
  - Services restart on failure

- [ ] **Volume Persistence**
  - Test database data persistence across restarts
  - Verify log files are accessible
  - Check data directory permissions (755)

- [ ] **Network Configuration**
  - Test internal service communication
  - Verify external port mappings (5000, 5432, 5050)
  - Configure firewall rules (block direct DB access)
  - Set up reverse proxy (nginx/traefik) if needed

---

### ✅ Database

- [ ] **Initialize Database**
  ```bash
  # Database schema is auto-applied via docker-entrypoint-initdb.d
  # Verify tables were created:
  docker compose exec postgres psql -U vnstock_user -d vnstock_db -c "\dt"
  ```

- [ ] **Run Migrations**
  ```bash
  docker compose exec postgres psql -U vnstock_user -d vnstock_db < database/migrations/001_add_system_tables.sql
  ```
  - Verify migrations applied successfully
  - Check for migration errors in logs
  - Validate table schemas match expected structure

- [ ] **Seed Initial Data**
  - Load stock list (31 default stocks)
  - Verify stock categories are correct
  - Test data collection jobs run successfully

- [ ] **Backup Strategy**
  ```bash
  # Test manual backup
  make db-backup

  # Schedule automated backups (cron)
  0 2 * * * cd /path/to/vn-stock-analytics && make db-backup
  ```

---

### ✅ API Endpoints

- [ ] **Health Check**
  ```bash
  curl http://localhost:5000/health
  # Should return: {"status": "healthy", "database": "connected", ...}
  ```

- [ ] **Critical Endpoints**
  - `GET /api/stocks` - Returns stock list
  - `GET /api/stock/VNM` - Returns stock details
  - `GET /api/stock/VNM/history?days=30` - Returns historical data
  - `GET /api/latest` - Returns latest prices
  - `GET /api/watchlist` - Returns watchlist
  - `POST /api/watchlist` - Updates watchlist
  - `GET /api/system-status` - Returns system status

- [ ] **Error Handling**
  - Test 404 responses (invalid stock symbol)
  - Test 400 responses (invalid parameters)
  - Test 500 responses (database down scenario)
  - Verify error logs are created

---

### ✅ Frontend

- [ ] **Static Assets**
  - All CSS files load correctly
  - All JavaScript files load correctly
  - Images and icons display properly
  - No 404 errors in browser console

- [ ] **Language Switching**
  - Test English ↔ Vietnamese switching
  - Verify all UI elements translate
  - Check HTML lang attribute updates
  - Test settings page translations

- [ ] **Responsive Design**
  - Test on mobile devices (320px-768px)
  - Test on tablets (768px-1200px)
  - Test on desktop (1200px+)
  - Verify all pages are responsive

- [ ] **Browser Compatibility**
  - Chrome/Edge (latest 2 versions)
  - Firefox (latest 2 versions)
  - Safari (latest 2 versions)
  - Test on different operating systems

---

### ✅ Data Collection

- [ ] **Stock Data Collection**
  ```bash
  # Manual test
  docker compose exec app python jobs/collect_stock_data.py
  ```
  - Verify 29/31 stocks collected successfully
  - Check for rate limit warnings (vnstock API)
  - Validate data saved to database
  - Test with rate limit delay (3.5s per request)

- [ ] **Scheduler Service**
  ```bash
  docker compose logs scheduler
  ```
  - Scheduler starts successfully
  - Jobs are registered (stock, indices, macro)
  - Cron schedules are correct
  - Market hours are configured (Mon-Fri, 9:00-15:00)

- [ ] **Data Quality**
  - Verify stock prices are realistic
  - Check for missing or null values
  - Validate historical data completeness
  - Test data refresh intervals work

---

### ✅ Monitoring & Logging

- [ ] **Application Logs**
  ```bash
  docker compose logs -f app
  docker compose logs -f scheduler
  ```
  - Logs are being written
  - Log format is readable
  - Error logs include stack traces
  - No sensitive data in logs

- [ ] **System Monitoring**
  - Set up health check monitoring (uptime robot, etc.)
  - Configure alerting for service failures
  - Monitor disk usage (logs, database)
  - Track API response times

- [ ] **Error Tracking**
  - Test error logging works
  - Verify activity log captures events
  - Check console.error statements removed
  - Test error handler utility works

---

### ✅ Performance

- [ ] **Load Testing**
  - Test with 10 concurrent users
  - Test with 50 concurrent users
  - Monitor database connection pool usage
  - Check API response times (<500ms target)

- [ ] **Database Performance**
  - Verify indexes are created
  - Test query performance on large datasets
  - Monitor connection pool utilization
  - Check for slow queries (>1s)

- [ ] **Asset Optimization**
  - Minimize CSS/JS files (if not done)
  - Enable gzip compression
  - Set proper cache headers
  - Optimize images (if any large images)

---

### ✅ Backup & Recovery

- [ ] **Database Backups**
  ```bash
  # Test backup
  make db-backup

  # Test restore
  make db-restore BACKUP_FILE=backup_20260217_120000.sql
  ```

- [ ] **Backup Schedule**
  - Set up automated daily backups (2 AM)
  - Configure backup retention (30 days)
  - Test backup to remote storage (S3, GCS)
  - Document restore procedure

- [ ] **Disaster Recovery Plan**
  - Document recovery steps
  - Test recovery from backup
  - Verify RTO/RPO targets
  - Train team on recovery process

---

### ✅ Documentation

- [ ] **API Documentation**
  - Review `/docs/api/API_REFERENCE.md`
  - Update any outdated endpoints
  - Document new features
  - Add usage examples

- [ ] **Deployment Documentation**
  - Update `/DOCKER_SETUP.md` with production notes
  - Document environment variables
  - Add troubleshooting section
  - Include rollback procedures

- [ ] **User Documentation**
  - Update `/README.md` with production URL
  - Document new features
  - Add getting started guide
  - Include support contacts

---

### ✅ Testing

- [ ] **Integration Tests**
  - API endpoints return expected data
  - Database queries work correctly
  - Background jobs execute successfully
  - Frontend displays data correctly

- [ ] **End-to-End Tests**
  - User can view stock list
  - User can view stock details
  - User can switch languages
  - User can save watchlist
  - Charts render correctly

- [ ] **Security Tests**
  - SQL injection protection (parameterized queries)
  - XSS protection (input validation)
  - CSRF protection (if applicable)
  - Rate limiting works (if configured)

---

### ✅ Final Checks

- [ ] **Domain & SSL**
  - Domain DNS configured
  - SSL certificate installed
  - HTTPS redirect configured
  - Certificate auto-renewal set up

- [ ] **Monitoring Setup**
  - Health check endpoint monitored
  - Error rate alerts configured
  - Disk space alerts set up
  - Database backup alerts enabled

- [ ] **Team Readiness**
  - Operations team trained
  - Deployment runbook reviewed
  - Rollback plan documented
  - Support contacts updated

- [ ] **Go-Live Preparation**
  - Announce maintenance window
  - Prepare rollback plan
  - Notify stakeholders
  - Schedule post-deployment review

---

## Deployment Commands

### Production Deployment

```bash
# 1. Pull latest code
git pull origin main

# 2. Validate secrets
python scripts/validate_secrets.py

# 3. Build and start services
docker compose build
docker compose up -d

# 4. Verify health
docker compose ps
curl http://localhost:5000/health

# 5. Check logs
docker compose logs -f
```

### Rollback Procedure

```bash
# 1. Stop services
docker compose down

# 2. Checkout previous version
git checkout <previous-commit-hash>

# 3. Restore database backup
make db-restore BACKUP_FILE=<backup-file>

# 4. Restart services
docker compose up -d

# 5. Verify rollback
curl http://localhost:5000/health
```

---

## Post-Deployment

### Immediate (0-1 hour)

- [ ] Monitor error logs for issues
- [ ] Check health endpoint every 5 minutes
- [ ] Verify data collection jobs run
- [ ] Test critical user flows
- [ ] Monitor system resources (CPU, memory, disk)

### Short-term (1-24 hours)

- [ ] Review API request patterns
- [ ] Check database performance
- [ ] Monitor data collection success rate
- [ ] Gather user feedback
- [ ] Address any reported issues

### Long-term (1-7 days)

- [ ] Analyze performance metrics
- [ ] Review error rates and patterns
- [ ] Optimize slow queries
- [ ] Plan improvements
- [ ] Schedule post-mortem meeting

---

## Support & Contacts

- **Technical Issues**: See logs and documentation
- **Security Concerns**: Run `python scripts/validate_secrets.py`
- **Database Issues**: Check connection pool settings
- **API Issues**: Review `/docs/api/API_REFERENCE.md`

---

## Useful Commands

```bash
# View all services status
docker compose ps

# View live logs
docker compose logs -f

# Restart a specific service
docker compose restart app

# Execute command in container
docker compose exec app python --version

# Database backup
make db-backup

# Database restore
make db-restore BACKUP_FILE=backup.sql

# Validate configuration
python config.py

# Validate secrets
python scripts/validate_secrets.py

# Trigger stock collection
docker compose exec app python jobs/collect_stock_data.py
```

---

**Deployment Date**: _________________
**Deployed By**: _________________
**Sign-off**: _________________

**Last Updated**: February 17, 2026
