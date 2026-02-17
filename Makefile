# Vietnamese Stock Analytics Platform - Docker Makefile
# Convenient shortcuts for common Docker operations

.PHONY: help build up down restart logs status clean backup restore dev prod

# Default target
help:
	@echo "Vietnamese Stock Analytics Platform - Docker Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make setup          - Initial setup (copy env file)"
	@echo "  make build          - Build Docker images"
	@echo ""
	@echo "Running:"
	@echo "  make up             - Start all services"
	@echo "  make down           - Stop all services"
	@echo "  make restart        - Restart all services"
	@echo "  make dev            - Start in development mode"
	@echo ""
	@echo "Monitoring:"
	@echo "  make logs           - View logs (all services)"
	@echo "  make logs-app       - View app logs"
	@echo "  make logs-scheduler - View scheduler logs"
	@echo "  make logs-db        - View database logs"
	@echo "  make status         - Show service status"
	@echo "  make health         - Check application health"
	@echo ""
	@echo "Database:"
	@echo "  make db-init        - Initialize database with data"
	@echo "  make db-shell       - Open PostgreSQL shell"
	@echo "  make db-backup      - Backup database"
	@echo "  make db-restore     - Restore database from backup"
	@echo "  make db-reset       - Reset database (WARNING: deletes data)"
	@echo ""
	@echo "Maintenance:"
	@echo "  make shell          - Open shell in app container"
	@echo "  make clean          - Stop and remove containers"
	@echo "  make clean-all      - Remove containers, volumes, and images"
	@echo "  make rebuild        - Rebuild and restart services"

# Setup
setup:
	@if [ ! -f .env ]; then \
		cp .env.docker .env; \
		echo "✅ Created .env file from .env.docker"; \
		echo "⚠️  Please edit .env and update passwords and secrets!"; \
	else \
		echo ".env file already exists"; \
	fi

# Build
build:
	docker compose build

rebuild:
	docker compose build --no-cache
	docker compose up -d

# Running
up:
	docker compose up -d
	@echo ""
	@echo "✅ Services started!"
	@echo "🌐 Web Interface: http://localhost:5000"
	@echo "📊 API Health: http://localhost:5000/health"
	@echo ""
	@echo "Run 'make logs' to view logs"
	@echo "Run 'make status' to check service status"

down:
	docker compose down

restart:
	docker compose restart

dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

prod:
	docker compose up -d

# Monitoring
logs:
	docker compose logs -f

logs-app:
	docker compose logs -f app

logs-scheduler:
	docker compose logs -f scheduler

logs-db:
	docker compose logs -f postgres

status:
	docker compose ps

health:
	@echo "Checking application health..."
	@curl -f http://localhost:5000/health 2>/dev/null && echo "✅ Application is healthy" || echo "❌ Application is unhealthy"

# Database operations
db-init:
	docker compose exec app python scripts/data/sync_data_to_db.py

db-shell:
	docker compose exec postgres psql -U vnstock_user -d vnstock_db

db-backup:
	@mkdir -p backups
	@BACKUP_FILE="backups/vnstock_backup_$$(date +%Y%m%d_%H%M%S).sql"; \
	docker compose exec postgres pg_dump -U vnstock_user vnstock_db > $$BACKUP_FILE && \
	echo "✅ Database backed up to $$BACKUP_FILE"

db-restore:
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make db-restore FILE=backups/vnstock_backup_YYYYMMDD_HHMMSS.sql"; \
		exit 1; \
	fi
	@cat $(FILE) | docker compose exec -T postgres psql -U vnstock_user -d vnstock_db
	@echo "✅ Database restored from $(FILE)"

db-reset:
	@echo "⚠️  WARNING: This will delete all database data!"
	@read -p "Are you sure? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		docker compose down -v; \
		docker compose up -d postgres; \
		sleep 5; \
		docker compose up -d; \
		echo "✅ Database reset complete"; \
	else \
		echo "Cancelled"; \
	fi

# Container operations
shell:
	docker compose exec app bash

shell-scheduler:
	docker compose exec scheduler bash

# Cleanup
clean:
	docker compose down
	@echo "✅ Containers stopped and removed"

clean-all:
	@echo "⚠️  WARNING: This will remove all containers, volumes, and images!"
	@read -p "Are you sure? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		docker compose down -v; \
		docker rmi $$(docker images 'vn-stock-analytics*' -q) 2>/dev/null || true; \
		echo "✅ Complete cleanup done"; \
	else \
		echo "Cancelled"; \
	fi

# Testing
test:
	docker compose exec app python -m pytest

test-coverage:
	docker compose exec app python -m pytest --cov=.

# Utility commands
ps:
	docker compose ps

top:
	docker compose top

stats:
	docker stats --no-stream

# Quick commands
start: up
stop: down
