#!/usr/bin/env python3
"""
Job Scheduler - Configuration-Based Automated Data Collection
Automatically runs data collection jobs based on settings in config.py and .env
"""

import sys
import os
from datetime import datetime
from pathlib import Path
import signal
import logging

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

# Import configuration
from config import (
    DATA_COLLECTION,
    MARKET_HOURS,
    DATA_SOURCES,
    COLLECTION_CONFIG,
    get_database_connection
)

# Import job modules
from jobs.collect_stock_data import StockDataCollector
from jobs.collect_macro_data import MacroDataCollector


# Setup logging from config
log_level = getattr(logging, COLLECTION_CONFIG['log_level'], logging.INFO)
logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(COLLECTION_CONFIG['log_file']),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('scheduler')


def log_activity(activity_type, activity, details, status='info'):
    """Log activity to database activity_log table"""
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO activity_log (activity_type, activity, details, status)
            VALUES (%s, %s, %s, %s);
        """, (activity_type, activity, details, status))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        logger.error(f"Failed to log activity to database: {e}")


class DataScheduler:
    """Manages scheduled data collection jobs"""

    def __init__(self):
        self.scheduler = BlockingScheduler()
        self.setup_jobs()
        self.setup_signal_handlers()

    def setup_signal_handlers(self):
        """Setup graceful shutdown on SIGINT/SIGTERM"""
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

    def shutdown(self, signum, frame):
        """Gracefully shutdown scheduler"""
        logger.info("Shutting down scheduler...")
        self.scheduler.shutdown()
        sys.exit(0)

    def collect_stocks(self):
        """Job: Collect stock data"""
        try:
            logger.info("=" * 70)
            logger.info("Starting stock data collection job")
            logger.info("=" * 70)
            log_activity('scheduler', 'Stock collection started', 'Automated stock data collection job triggered', 'info')
            collector = StockDataCollector()
            collector.run()
            log_activity('collection', 'Stock collection completed', 'Stock data collection finished successfully', 'success')
        except Exception as e:
            logger.error(f"Stock collection job failed: {e}", exc_info=True)
            log_activity('collection', 'Stock collection failed', str(e), 'error')

    def collect_macro(self):
        """Job: Collect macro data"""
        try:
            logger.info("=" * 70)
            logger.info("Starting macro data collection job")
            logger.info("=" * 70)
            log_activity('scheduler', 'Macro collection started', 'Automated macro data collection job triggered', 'info')
            collector = MacroDataCollector()
            collector.run()
            log_activity('collection', 'Macro collection completed', 'Macro data collection finished successfully', 'success')
        except Exception as e:
            logger.error(f"Macro collection job failed: {e}", exc_info=True)
            log_activity('collection', 'Macro collection failed', str(e), 'error')

    def setup_jobs(self):
        """Setup all scheduled jobs based on configuration"""

        if not DATA_COLLECTION['enabled']:
            logger.warning("⚠️  Automated data collection is DISABLED in config")
            logger.warning("   Set AUTO_COLLECT_ENABLED=true in .env to enable")
            return

        logger.info("Setting up scheduled jobs from configuration...")
        logger.info("")

        jobs_scheduled = 0

        # ==================================================================
        # STOCK DATA COLLECTION
        # ==================================================================
        if DATA_COLLECTION['stock']['enabled']:
            stock_config = DATA_COLLECTION['stock']
            market_hours = MARKET_HOURS

            # Convert interval to hours/minutes for cron
            interval_seconds = stock_config['interval']

            if stock_config['market_hours_only']:
                # Schedule during market hours only
                hour_range = f"{market_hours['open_hour']}-{market_hours['close_hour']}"

                # Calculate minute interval
                if interval_seconds >= 3600:  # Hourly or more
                    hours_interval = interval_seconds // 3600
                    minute = 5  # Run at 5 minutes past

                    self.scheduler.add_job(
                        self.collect_stocks,
                        CronTrigger(
                            day_of_week=market_hours['days'],
                            hour=f"{market_hours['open_hour']}-{market_hours['close_hour']}/{hours_interval}",
                            minute=minute
                        ),
                        id='stock_data_market_hours',
                        name=f'Stock Data Collection (Every {hours_interval}h during market)',
                        replace_existing=True,
                        max_instances=1
                    )

                    logger.info(f"✓ Stock collection: Every {hours_interval} hour(s) during market hours")
                    logger.info(f"  Market hours: {market_hours['days']} {hour_range}:00")
                    jobs_scheduled += 1
                else:
                    # Sub-hourly collection during market hours
                    minutes_interval = interval_seconds // 60

                    self.scheduler.add_job(
                        self.collect_stocks,
                        IntervalTrigger(seconds=interval_seconds),
                        id='stock_data_interval',
                        name=f'Stock Data Collection (Every {minutes_interval} min)',
                        replace_existing=True,
                        max_instances=1
                    )

                    logger.info(f"✓ Stock collection: Every {minutes_interval} minute(s)")
                    jobs_scheduled += 1

                # End of day collection
                if stock_config['end_of_day']:
                    self.scheduler.add_job(
                        self.collect_stocks,
                        CronTrigger(
                            day_of_week=market_hours['days'],
                            hour=market_hours['close_hour'],
                            minute=30
                        ),
                        id='stock_data_eod',
                        name='Stock Data Collection (End of Day)',
                        replace_existing=True,
                        max_instances=1
                    )

                    logger.info(f"✓ Stock collection: End of day at {market_hours['close_hour']}:30")
                    jobs_scheduled += 1
            else:
                # Schedule at fixed interval regardless of market hours
                self.scheduler.add_job(
                    self.collect_stocks,
                    IntervalTrigger(seconds=interval_seconds),
                    id='stock_data_interval',
                    name=f'Stock Data Collection (Every {interval_seconds}s)',
                    replace_existing=True,
                    max_instances=1
                )

                hours = interval_seconds // 3600
                minutes = (interval_seconds % 3600) // 60
                interval_str = f"{hours}h {minutes}m" if hours else f"{minutes}m"
                logger.info(f"✓ Stock collection: Every {interval_str} (24/7)")
                jobs_scheduled += 1
        else:
            logger.info("⊗ Stock collection: Disabled")

        logger.info("")

        # ==================================================================
        # MARKET INDICES COLLECTION
        # ==================================================================
        if DATA_COLLECTION['indices']['enabled']:
            indices_config = DATA_COLLECTION['indices']
            interval_seconds = indices_config['interval']

            if indices_config['market_hours_only']:
                # During market hours only
                self.scheduler.add_job(
                    self.collect_macro,
                    CronTrigger(
                        day_of_week=MARKET_HOURS['days'],
                        hour=f"{MARKET_HOURS['open_hour']}-{MARKET_HOURS['close_hour']}",
                        minute=f"*/{interval_seconds // 60}"
                    ),
                    id='indices_market_hours',
                    name=f'Market Indices (Every {interval_seconds // 60} min during market)',
                    replace_existing=True,
                    max_instances=1
                )

                logger.info(f"✓ Indices collection: Every {interval_seconds // 60} minute(s) during market")
                jobs_scheduled += 1
            else:
                # 24/7 collection
                self.scheduler.add_job(
                    self.collect_macro,
                    IntervalTrigger(seconds=interval_seconds),
                    id='indices_interval',
                    name=f'Market Indices (Every {interval_seconds // 60} min)',
                    replace_existing=True,
                    max_instances=1
                )

                logger.info(f"✓ Indices collection: Every {interval_seconds // 60} minute(s) (24/7)")
                jobs_scheduled += 1
        else:
            logger.info("⊗ Indices collection: Disabled")

        logger.info("")

        # ==================================================================
        # MACRO INDICATORS COLLECTION
        # ==================================================================
        if DATA_COLLECTION['macro']['enabled']:
            macro_config = DATA_COLLECTION['macro']

            # Daily update at specified hour
            if macro_config['daily_update']:
                self.scheduler.add_job(
                    self.collect_macro,
                    CronTrigger(
                        hour=macro_config['daily_update_hour'],
                        minute=0
                    ),
                    id='macro_daily',
                    name=f"Macro Data (Daily at {macro_config['daily_update_hour']}:00)",
                    replace_existing=True,
                    max_instances=1
                )

                logger.info(f"✓ Macro collection: Daily at {macro_config['daily_update_hour']}:00")
                jobs_scheduled += 1

            # Interval-based collection
            interval_seconds = macro_config['interval']
            if interval_seconds > 0 and interval_seconds != 86400:  # Not daily
                self.scheduler.add_job(
                    self.collect_macro,
                    IntervalTrigger(seconds=interval_seconds),
                    id='macro_interval',
                    name=f'Macro Data (Every {interval_seconds // 3600}h)',
                    replace_existing=True,
                    max_instances=1
                )

                hours = interval_seconds // 3600
                logger.info(f"✓ Macro collection: Every {hours} hour(s)")
                jobs_scheduled += 1
        else:
            logger.info("⊗ Macro collection: Disabled")

        logger.info("")
        logger.info("=" * 70)
        logger.info(f"Total jobs scheduled: {jobs_scheduled}")
        logger.info("=" * 70)

    def run_now(self):
        """Run all jobs immediately (for testing)"""
        logger.info("\n🚀 Running all jobs immediately for testing...\n")
        self.collect_stocks()
        self.collect_macro()
        logger.info("\n✅ All jobs completed\n")

    def start(self):
        """Start the scheduler"""
        logger.info("=" * 70)
        logger.info("📅 Stock Data Scheduler Starting")
        logger.info("=" * 70)
        logger.info(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("\nScheduled Jobs:")

        for job in self.scheduler.get_jobs():
            logger.info(f"  • {job.name}")
            logger.info(f"    Trigger: {job.trigger}")
            # Handle next_run_time which may not be available before scheduler starts
            try:
                next_run = job.next_run_time if hasattr(job, 'next_run_time') else 'Pending start'
                logger.info(f"    Next run: {next_run}")
            except:
                logger.info(f"    Next run: Pending start")
            logger.info("")

        logger.info("=" * 70)
        logger.info("Scheduler is running. Press Ctrl+C to stop.")
        logger.info("=" * 70)
        logger.info("")

        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            logger.info("\nScheduler stopped by user")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Stock Data Scheduler')
    parser.add_argument(
        '--now',
        action='store_true',
        help='Run all jobs immediately (for testing)'
    )
    parser.add_argument(
        '--stock-only',
        action='store_true',
        help='Run stock collection only'
    )
    parser.add_argument(
        '--macro-only',
        action='store_true',
        help='Run macro collection only'
    )

    args = parser.parse_args()

    scheduler = DataScheduler()

    if args.now:
        # Run all jobs immediately
        scheduler.run_now()
    elif args.stock_only:
        # Run stock collection only
        logger.info("Running stock data collection...")
        scheduler.collect_stocks()
    elif args.macro_only:
        # Run macro collection only
        logger.info("Running macro data collection...")
        scheduler.collect_macro()
    else:
        # Start scheduler daemon
        scheduler.start()


if __name__ == '__main__':
    main()
