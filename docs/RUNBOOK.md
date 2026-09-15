\# Runbook — Sales Automation Pipeline



\## 1. Purpose

Automates ingestion, validation, reporting, and notification for daily sales CSVs.



\## 2. Prerequisites

\- Python 3.10+

\- `pip install -r requirements.txt`

\- Write access to `data/` and `logs/`



\## 3. Configuration

Edit `config.yaml`. Key fields:

\- `paths.\*` — input/output folders

\- `schedule.cron` — standard 5-field cron

\- `validation.\*` — thresholds

\- `notification.channel` — `console` or `file`



\## 4. Standard Operations



\### Run once

&#x20;   python run.py --once



\### Run on schedule

&#x20;   python run.py --schedule



\### Run tests

&#x20;   pytest -v

&#x20;   pytest --cov=src/sales\_pipeline --cov-report=term-missing



\## 5. Deployment



\### Option A — Windows Task Scheduler

1\. Open Task Scheduler

2\. Create Basic Task

3\. Trigger: Daily at 07:00

4\. Action: Start a program

5\. Program: `D:\\path\\to\\.venv\\Scripts\\python.exe`

6\. Arguments: `run.py --once`

7\. Start in: `D:\\path\\to\\project`



\### Option B — systemd (Linux)

&#x20;   \[Unit]

&#x20;   Description=Sales Automation Pipeline

&#x20;   \[Service]

&#x20;   WorkingDirectory=/opt/sales\_pipeline

&#x20;   ExecStart=/opt/sales\_pipeline/.venv/bin/python run.py --schedule

&#x20;   Restart=on-failure

&#x20;   \[Install]

&#x20;   WantedBy=multi-user.target



\## 6. Monitoring

\- `logs/pipeline.log` — per-run entries

\- `data/reports/` — timestamped Excel + CSV

\- `data/archive/` — processed source files



\## 7. Troubleshooting

| Symptom | Cause | Fix |

|---|---|---|

| "No files found" | Empty inbox | Drop CSVs in `data/inbox/` |

| "Missing required columns" | Bad header | Fix CSV header |

| "Columns exceed null threshold" | Too many blanks | Clean source or raise threshold |

| Report not written | Permissions | Check `data/reports/` |

| Scheduler not firing | Wrong cron | Verify `config.yaml` |



\## 8. Recovery

\- Move files from `data/archive/` back to `data/inbox/` to reprocess.

\- Delete timestamped reports to force regeneration.



\## 9. Backup

\- Back up `data/`, `config.yaml`, `logs/` nightly.

