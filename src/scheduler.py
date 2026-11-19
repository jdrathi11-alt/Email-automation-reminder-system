"""Scheduler module: keeps the program running and triggers jobs on a timetable.

Uses only the standard library (time + threading) so the project runs anywhere
without extra packages. In a real company this would be a cron job, Airflow DAG,
or cloud scheduler.
"""
import logging
import threading
import time


def start_scheduler(job, interval_minutes=1):
    """Run `job` repeatedly every `interval_minutes` minutes until Ctrl+C."""
    def loop():
        while True:
            job()
            time.sleep(interval_minutes * 60)

    logging.info("Scheduler started: job runs every %s minute(s).", interval_minutes)
    print(f"[INFO] Scheduler started. Running job every {interval_minutes} minute(s). Press Ctrl+C to stop.")
    try:
        thread = threading.Thread(target=loop, daemon=True)
        thread.start()
        # Keep the main thread alive.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user.")
        print("[INFO] Scheduler stopped.")
