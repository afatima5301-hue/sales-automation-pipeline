\# Sales Automation Pipeline



Automated workflow for ingesting sales CSVs, validating data, producing KPI

reports (Excel + CSV), notifying stakeholders, and running on a schedule.



\## Features

\- Scheduled ingestion (APScheduler) or one-shot CLI

\- Strict validation (schema, nulls, value ranges)

\- KPI aggregation (revenue, orders, top products, region totals)

\- Excel + CSV report generation

\- Pluggable notification (console / file)

\- Archive-on-success for idempotent reruns

\- Unit, integration, and performance tests



\## Quick Start

&#x20;   python -m venv .venv

&#x20;   .venv\\Scripts\\activate

&#x20;   pip install -r requirements.txt

&#x20;   python run.py --once



\## Tests

&#x20;   pytest -v

&#x20;   pytest --cov=src/sales\_pipeline --cov-report=term-missing



\## Schedule Mode

&#x20;   python run.py --schedule



\## Project Structure

&#x20;   src/sales\_pipeline/    # library code

&#x20;   tests/                 # unit + integration + perf

&#x20;   data/inbox/            # drop CSV files here

&#x20;   data/archive/          # processed files

&#x20;   data/reports/          # generated reports

&#x20;   docs/                  # runbook, report, screenshots

&#x20;   run.py                 # CLI entry point



\## Docs

\- `docs/RUNBOOK.md` — operations \& deployment

\- `docs/REPORT.md` — design, challenges, results



\## Author

Aptura Tech Solutions Python Intern — Week 4 Final Task

