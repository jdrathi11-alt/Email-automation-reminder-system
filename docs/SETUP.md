# Setup Guide

## Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# edit .env with your Gmail app password
python main.py --dry-run
```

## Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env with your Gmail app password
python main.py --dry-run
```

## Real email mode
```bash
python main.py
```

## Expected output
- Terminal: number of processed reminders
- `logs/automation.log`: detailed send log
- `outputs/report.csv`: status report
