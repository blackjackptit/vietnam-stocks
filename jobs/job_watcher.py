#!/usr/bin/env python3
"""
Job Watcher Service
Monitors database signals and triggers data collection jobs
Allows UI to control jobs through database signals
"""

import sys
import os
import time
import signal
import logging
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import get_database_connection
from jobs.collect_stock_data import StockDataCollector
from jobs.collect_macro_data import MacroDataCollector

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/job_watcher.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('job_watcher')


class JobWatcher:
    """Watches for job trigger signals in database and executes jobs"""

    def __init__(self):
        self.running = True
        self.check_interval = 5  # Check every 5 seconds
        self.setup_signal_handlers()

    def setup_signal_handlers(self):
        """Setup graceful shutdown on SIGINT/SIGTERM"""
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

    def shutdown(self, signum, frame):
        """Gracefully shutdown watcher"""
        logger.info("Shutting down job watcher...")
        self.running = False
        sys.exit(0)

    def get_control_value(self, key):
        """Get a control value from database"""
        try:
            conn = get_database_connection()
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT control_value FROM system_controls
                    WHERE control_key = %s;
                """, (key,))
                result = cursor.fetchone()
                conn.close()
                return result[0] if result else None
        except Exception as e:
            logger.error(f"Error getting control value for {key}: {e}")
            return None

    def set_control_value(self, key, value):
        """Set a control value in database"""
        try:
            conn = get_database_connection()
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE system_controls
                    SET control_value = %s, updated_at = NOW()
                    WHERE control_key = %s;
                """, (str(value), key))
                conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Error setting control value for {key}: {e}")
            return False

    def log_activity(self, activity_type, activity, details, status='success'):
        """Log activity to database"""
        try:
            conn = get_database_connection()
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO activity_log (activity_type, activity, details, status)
                    VALUES (%s, %s, %s, %s);
                """, (activity_type, activity, details, status))
                conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error logging activity: {e}")

    def check_and_run_stock_collection(self):
        """Check for stock collection trigger and run if needed"""
        trigger = self.get_control_value('job.collect_stock.trigger')

        if trigger == 'true':
            logger.info("Stock collection triggered!")

            # Reset trigger
            self.set_control_value('job.collect_stock.trigger', 'false')

            # Update status
            self.set_control_value('system.collection_status', 'collecting_stocks')

            try:
                # Run collection
                logger.info("Starting stock data collection...")
                collector = StockDataCollector()
                collector.run()

                # Update last collection time
                self.set_control_value('system.last_stock_collection', datetime.now().isoformat())

                # Log success
                self.log_activity(
                    'collection',
                    'Stock data collected',
                    'Stock collection completed successfully',
                    'success'
                )

                logger.info("Stock collection completed successfully")

            except Exception as e:
                logger.error(f"Stock collection failed: {e}")
                self.log_activity(
                    'collection',
                    'Stock collection failed',
                    str(e),
                    'error'
                )

            finally:
                # Reset status
                self.set_control_value('system.collection_status', 'idle')

    def check_and_run_macro_collection(self):
        """Check for macro collection trigger and run if needed"""
        trigger = self.get_control_value('job.collect_macro.trigger')

        if trigger == 'true':
            logger.info("Macro collection triggered!")

            # Reset trigger
            self.set_control_value('job.collect_macro.trigger', 'false')

            # Update status
            self.set_control_value('system.collection_status', 'collecting_macro')

            try:
                # Run collection
                logger.info("Starting macro data collection...")
                collector = MacroDataCollector()
                collector.run()

                # Update last collection time
                self.set_control_value('system.last_macro_collection', datetime.now().isoformat())

                # Log success
                self.log_activity(
                    'collection',
                    'Macro data collected',
                    'Macro collection completed successfully',
                    'success'
                )

                logger.info("Macro collection completed successfully")

            except Exception as e:
                logger.error(f"Macro collection failed: {e}")
                self.log_activity(
                    'collection',
                    'Macro collection failed',
                    str(e),
                    'error'
                )

            finally:
                # Reset status
                self.set_control_value('system.collection_status', 'idle')

    def watch(self):
        """Main watch loop"""
        logger.info("=" * 70)
        logger.info("🔍 Job Watcher Started")
        logger.info("=" * 70)
        logger.info(f"Checking for job triggers every {self.check_interval} seconds")
        logger.info("Press Ctrl+C to stop")
        logger.info("=" * 70)
        logger.info("")

        # Log startup
        self.log_activity(
            'system',
            'Job watcher started',
            'Monitoring for job trigger signals',
            'info'
        )

        iteration = 0
        while self.running:
            try:
                iteration += 1

                # Check for stock collection trigger
                self.check_and_run_stock_collection()

                # Check for macro collection trigger
                self.check_and_run_macro_collection()

                # Log heartbeat every minute (12 iterations at 5s interval)
                if iteration % 12 == 0:
                    logger.debug(f"Heartbeat - Iteration {iteration}")

                # Wait before next check
                time.sleep(self.check_interval)

            except Exception as e:
                logger.error(f"Error in watch loop: {e}")
                time.sleep(self.check_interval)


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Job Watcher Service')
    parser.add_argument(
        '--interval',
        type=int,
        default=5,
        help='Check interval in seconds (default: 5)'
    )

    args = parser.parse_args()

    watcher = JobWatcher()
    watcher.check_interval = args.interval
    watcher.watch()


if __name__ == '__main__':
    main()
