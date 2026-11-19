# Email Automation & Reminder System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Mode](https://img.shields.io/badge/Mode-Dry--Run%20Safe-green)
![Status](https://img.shields.io/badge/Status-Student%20Project-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A beginner-friendly Python project that simulates a real business email automation platform. It reads contacts and reminders from CSV files, personalizes email templates, schedules messages, sends them through Gmail SMTP, logs outcomes, and creates a CSV report.

Built as proof of work for **Python Developer, Automation, Operations, HR, Admin, and Business Productivity** roles.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Command-Line Options](#command-line-options)
- [Sample Output](#sample-output)
- [Sample Report](#sample-report)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Roadmap](#roadmap)
- [Learning Outcomes](#learning-outcomes)
- [Documentation](#documentation)
- [License](#license)

---

## Project Overview

Companies send thousands of reminder emails every day — payment follow-ups, meeting alerts, webinar invitations, task notifications. Doing this by hand is slow, error-prone, and impossible to audit.

This project replaces that manual work with one Python command: read a contact list, match it to a reminder list, fill an email template, send through Gmail SMTP, log every outcome, and write a CSV report.

---

## Problem Statement

> "A training company emails 50 students every day about upcoming classes. A person doing this manually spends an hour a day, makes naming mistakes, and has no record of who was emailed. Build a Python system that automates this workflow safely, with logs and a report as proof."

This project solves it with **CSV-driven automation, template personalization, local scheduling, logging, and reporting** — all running locally with dummy data.

---

## Key Features

- [x] CSV contact and reminder management (pandas)
- [x] Personalized email templates with `{{placeholder}}` syntax
- [x] Gmail SMTP sending with TLS (port 587)
- [x] Dry-run mode — full pipeline, zero real emails
- [x] Local scheduling with a threaded job runner
- [x] Logging of every send, failure, and status
- [x] CSV report generation for audit and proof
- [x] Credentials via environment variables (never hard-coded)
- [x] Per-email error handling — one failure never stops the batch

---

## How It Works

```
contacts.csv ──┐
               ├──> personalization ─> scheduler ─> Gmail SMTP ─> logging ─> report.csv
reminders.csv ─┤         ^
               │    template.html
templates/ ────┘
```

1. **Input** — contacts, reminders, and an email template.
2. **Match** — each reminder is joined to its contact by `contact_id`.
3. **Personalize** — placeholders are replaced with real values.
4. **Send** — the email goes out via SMTP, or is simulated in dry-run.
5. **Track** — every outcome is logged and written to `outputs/report.csv`.

See `docs/ARCHITECTURE.md` for the full design.

---

## Tech Stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| Language | Python 3.10+ | Core automation |
| Data | pandas | CSV reading and joining |
| Email | smtplib, email.mime | SMTP sending with TLS |
| Scheduling | threading, time | Local job runner |
| Config | environment variables, `.env` | Secure credentials |
| Observability | logging | Timestamped audit trail |
| Output | CSV | Report generation |

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/jdrathi11-alt/Email-automation-reminder-system.git
cd Email-automation-reminder-system

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gmail app password
copy .env.example .env         # Windows
cp .env.example .env           # Mac/Linux

# 5. Run in dry-run mode (safe, no real emails)
python main.py --dry-run

# 6. Send real emails
python main.py
```

---

## Configuration

Create a `.env` file (never commit it). The repo ships with `.env.example`.

| Variable | Default | Description |
| --- | --- | --- |
| `EMAIL_USER` | — | Your Gmail address |
| `EMAIL_PASSWORD` | — | 16-character Gmail **app password** (not your account password) |
| `SMTP_HOST` | `smtp.gmail.com` | SMTP server |
| `SMTP_PORT` | `587` | SMTP port with STARTTLS |
| `DRY_RUN` | `true` | Set `false` to send real email |

---

## Command-Line Options

| Flag | Effect |
| --- | --- |
| `--dry-run` | Simulate sends; no SMTP connection |
| `--schedule` | Keep running and trigger the job every minute |
| *(none)* | Send real emails using `.env` credentials |

---

## Sample Output

```
[INFO] Dry-run mode ON: no real emails will be sent.
[DRY_RUN] alice@example.com - Webinar Reminder: Python Automation
[DRY_RUN] bob@example.com - Meeting Reminder: Quarterly Review
[DRY_RUN] charlie@example.com - Payment Reminder: Invoice #1024
Processed 5 reminders. Report saved to outputs/report.csv
```

---

## Sample Report

`outputs/report.csv` after a run:

| status | recipient | subject | type | scheduled_time |
| --- | --- | --- | --- | --- |
| DRY_RUN | alice@example.com | Webinar Reminder | Webinar | 2026-11-20 10:00 |
| DRY_RUN | bob@example.com | Meeting Reminder | Meeting | 2026-11-20 14:00 |
| DRY_RUN | charlie@example.com | Payment Reminder | Payment | 2026-11-21 09:00 |

Full log of every run: `logs/automation.log`.

---

## Project Structure

```
Email-Automation-Reminder-System/
├── data/                 # CSV inputs: contacts.csv, reminders.csv
├── templates/            # email.html, reminder_template.txt
├── src/                  # email_sender, email_automation, scheduler, report_generator
├── outputs/              # Generated report.csv (gitignored)
├── logs/                 # automation.log (gitignored)
├── images/               # Screenshots referenced below
├── docs/                 # Setup, architecture, GitHub, interview prep
├── main.py               # Entry point
├── requirements.txt
├── .env.example          # Template for credentials (safe to commit)
├── .gitignore
├── README.md
└── LICENSE
```

---

## Screenshots

Capture these and save them in `images/` with the exact names below; the embeds will render automatically.

| File | What to capture |
| --- | --- |
| `images/01-folder-structure.png` | Project folder in Explorer or VS Code |
| `images/02-contacts-csv.png` | `data/contacts.csv` open in Excel |
| `images/03-reminders-csv.png` | `data/reminders.csv` open in Excel |
| `images/04-template.png` | `templates/email.html` in the editor |
| `images/05-dry-run.png` | Terminal running `python main.py --dry-run` |
| `images/06-schedule.png` | Terminal running `--schedule` |
| `images/07-log.png` | `logs/automation.log` contents |
| `images/08-report.png` | `outputs/report.csv` open in Excel |
| `images/09-github.png` | Repository page with README |

Example embed once the file exists:

```html
<!-- <img src="images/05-dry-run.png" width="700" alt="Dry-run terminal output"> -->
```

Full capture checklist: `docs/SCREENSHOT_GUIDE.md`.

---

## Roadmap

- [ ] Streamlit dashboard for run history (Option C)
- [ ] SQLite storage instead of CSV
- [ ] Multiple template types (payment, webinar, task)
- [ ] Retry logic for failed sends

---

## Learning Outcomes

- CSV file handling with pandas
- Email protocols and SMTP with `smtplib`
- String templating and personalization
- Error handling and logging
- Local scheduling with threading
- Secure credential handling with environment variables
- GitHub project documentation

---

## Documentation

| File | Contents |
| --- | --- |
| `docs/PROJECT_GUIDE.md` | Full 14-section project guide |
| `docs/SETUP.md` | Installation (Windows / Mac / Linux) |
| `docs/ARCHITECTURE.md` | System design and data flow |
| `docs/GITHUB_GUIDE.md` | Upload steps, commit messages, security rules |
| `docs/INTERVIEW_PREP.md` | 10 interview questions with strong answers |
| `docs/SCREENSHOT_GUIDE.md` | What screenshots to capture |
| `docs/PROOF_PLAN.md` | Day-wise proof plan with commits |

---

## License

This project is licensed under the MIT License — see `LICENSE` for details.

---

## Author
**Jayesh Rathi** — 3rd Year IT Student, Government College of Engineering, Amravati  
[LinkedIn](https://www.linkedin.com/in/jayesh-rathi-5ab8973b6) | [Email](mailto:jayeshrathinew@gmail.com)
