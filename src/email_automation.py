"""Core automation logic: read data, personalize templates, send reminders."""
import logging
import os
from pathlib import Path

import pandas as pd

from .email_sender import send_email
from .report_generator import generate_report


def setup_logging():
    """Create logs folder and configure logging AFTER folders exist."""
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        filename="logs/automation.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def load_contacts(path="data/contacts.csv"):
    """Load the contact list from a CSV file."""
    return pd.read_csv(path)


def load_reminders(path="data/reminders.csv"):
    """Load the reminder list from a CSV file."""
    return pd.read_csv(path)


def render_template(template_text, context):
    """Replace {{placeholders}} in a template with real values."""
    for key, value in context.items():
        template_text = template_text.replace("{{" + key + "}}", str(value))
    return template_text


def run_automation(dry_run=True):
    """Run one full cycle of the email automation pipeline."""
    setup_logging()
    Path("outputs").mkdir(exist_ok=True)

    contacts = load_contacts()
    reminders = load_reminders()
    html_template = Path("templates/email.html").read_text()

    results = []
    for reminder in reminders.to_dict(orient="records"):
        # Find the contact this reminder belongs to.
        match = contacts[contacts["contact_id"] == reminder["contact_id"]]
        if match.empty:
            logging.warning("Reminder %s: contact_id %s not found.",
                            reminder["reminder_id"], reminder["contact_id"])
            continue
        contact = match.iloc[0]

        # Build personalized values.
        context = {
            "name": contact["name"],
            "company": contact["company"],
            "subject": reminder["subject"],
            "message": reminder["message"],
        }
        body = render_template(html_template, context)

        # Send (or simulate) the email.
        result = send_email(
            os.getenv("SMTP_HOST", "smtp.gmail.com"),
            int(os.getenv("SMTP_PORT", 587)),
            os.getenv("EMAIL_USER", ""),
            os.getenv("EMAIL_PASSWORD", ""),
            contact["email"],
            reminder["subject"],
            body,
            dry_run=dry_run,
        )
        result["reminder_id"] = reminder["reminder_id"]
        result["type"] = reminder["type"]
        result["scheduled_time"] = str(reminder["scheduled_time"])
        results.append(result)

        logging.info("%s | %s | %s", result["status"], result["recipient"], result["subject"])
        print(f"[{result['status']}] {result['recipient']} - {result['subject']}")

    report_path = generate_report(results)
    logging.info("Run complete. %s reminders processed. Report: %s", len(results), report_path)
    return results, report_path
