# Interview Preparation

## 1. Explain your project.
This project automates email reminders using Python. It reads contact and reminder data from CSV files, personalizes email templates, schedules messages, sends them via Gmail SMTP, logs results, and generates a CSV report. It demonstrates file handling, templating, SMTP, error handling, logging, and reporting.

## 2. Why did you build this project?
To simulate a real business automation system and learn how Python can reduce repetitive communication tasks for HR, operations, sales, and training teams.

## 3. What libraries did you use?
pandas for data handling, schedule for local scheduling, python-dotenv for credentials, smtplib and email.mime for sending emails, and logging for tracking outcomes.

## 4. How do you protect credentials?
Credentials are stored in environment variables and never committed to GitHub. A `.env.example` file shows the required format.

## 5. What is dry-run mode?
Dry-run mode simulates email sending without connecting to SMTP or sending real messages. It helps test the workflow safely.

## 6. How do you personalize emails?
Templates use placeholders like `{{name}}` and `{{company}}`. The code replaces placeholders with values from the contact and reminder data.

## 7. How do you handle errors?
The email sender uses try/except blocks, logs failures, and includes error details in the report.

## 8. What outputs are generated?
A log file and a CSV report showing status, recipient, subject, reminder type, and scheduled time.

## 9. How would this work in a real company?
It would connect to a database or CRM, use approved templates, integrate with a task scheduler, and send through a secure SMTP service with monitoring.

## 10. What did you learn?
Practical automation, secure credential handling, CSV processing, email protocols, logging, reporting, and project documentation.
