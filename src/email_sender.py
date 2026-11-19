"""Email sending module for the Email Automation & Reminder System."""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(smtp_host, smtp_port, username, password, recipient, subject, html_body, dry_run=False):
    """Send an HTML email or simulate it in dry-run mode."""
    if dry_run:
        return {"status": "DRY_RUN", "recipient": recipient, "subject": subject}

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = username
    msg["To"] = recipient
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(username, recipient, msg.as_string())
        return {"status": "SENT", "recipient": recipient, "subject": subject}
    except Exception as exc:
        return {"status": "FAILED", "recipient": recipient, "subject": subject, "error": str(exc)}
