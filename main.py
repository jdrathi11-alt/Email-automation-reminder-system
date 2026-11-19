"""Entry point for the Email Automation & Reminder System.

Usage:
    python main.py --dry-run    # simulate sending (no real emails)
    python main.py              # send real emails via Gmail SMTP
    python main.py --schedule   # keep running and send reminders on a schedule
"""
import argparse
import os

from src.email_automation import run_automation
from src.scheduler import start_scheduler


def load_config():
    """Load configuration from environment variables or a .env file.

    Reads KEY=VALUE lines from a .env file if present.
    Real secrets stay out of source control this way.
    """
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip())


def main():
    load_config()

    parser = argparse.ArgumentParser(description="Email Automation & Reminder System")
    parser.add_argument("--dry-run", action="store_true",
                        help="Simulate emails without sending them")
    parser.add_argument("--schedule", action="store_true",
                        help="Keep the program running and send reminders on a schedule")
    args = parser.parse_args()

    dry_run = args.dry_run or os.getenv("DRY_RUN", "true").lower() == "true"

    if dry_run:
        print("[INFO] Dry-run mode ON: no real emails will be sent.")

    if args.schedule:
        # Schedule the automation to run every N minutes (change as needed).
        start_scheduler(lambda: run_automation(dry_run=dry_run), interval_minutes=1)
    else:
        results, report_path = run_automation(dry_run=dry_run)
        print(f"Processed {len(results)} reminders. Report saved to {report_path}")


if __name__ == "__main__":
    main()
