# Project Architecture

## Input
- contact CSV: contact details
- reminder CSV: reminder type, message, schedule
- email template: reusable message format

## Processing
1. Read contacts
2. Read reminders
3. Match contact to reminder
4. Personalize template
5. Schedule or send email
6. Track status

## Output
- sent emails
- failed emails
- reminder logs
- CSV report

## Data flow
```
contacts.csv + reminders.csv + template
        ↓
   personalization
        ↓
   scheduler / sender
        ↓
   Gmail SMTP (or dry-run)
        ↓
   logging + report.csv
```
