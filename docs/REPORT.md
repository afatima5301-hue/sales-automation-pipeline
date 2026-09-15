\# Final Report — Sales Automation Pipeline



\## 1. Objective

Deliver a production-style automated workflow: ingest → validate → transform

→ report → notify, on a schedule, with tests and documentation.



\## 2. Key Decisions

\- \*\*pandas\*\* for tabular work (fast, expressive, well-tested)

\- \*\*openpyxl\*\* for Excel output (no external binaries required)

\- \*\*APScheduler\*\* instead of OS cron — same code runs cross-platform

\- \*\*YAML config\*\* so ops can change behavior without code edits

\- \*\*Pluggable notification\*\* (console/file) for extensibility

\- \*\*Archive-on-success\*\* for idempotency and raw data preservation



\## 3. Challenges \& Solutions

| Challenge | Solution |

|---|---|

| Bad CSVs crashing the run | Per-file try/except; failures collected, not fatal |

| Bad date formats | `pd.to\_datetime(errors="coerce")`, drop NaT |

| Region label noise ("north", "NORTH") | `.str.strip().str.title()` |

| Test isolation | `tmp\_path` fixtures; no shared state |

| PowerShell escape issues | Used Notepad for file creation |



\## 4. Results

\- End-to-end pipeline working on real CSV input

\- 15 tests passing (unit + integration + performance)

\- Coverage: \~90% on `src/sales\_pipeline`

\- Excel report with 4 sheets: KPIs, Data, ByRegion, TopProducts

\- 100k rows transformed in < 5 seconds

\- Real run: 2 files → 6 rows → revenue 220.0 in 0.536s



\## 5. Validation \& QA Evidence

\- `pytest -v` output showing 15 passed

\- Coverage report

\- Sample generated Excel + CSV

\- Log entries for successful runs

\- Screenshots of terminal output and logs



\## 6. Limitations

\- No database persistence (files only)

\- Email/Slack notification is a stub (console/file)

\- No PDF reporting (Excel + CSV only)

\- No authentication / secret management



\## 7. Future Improvements

\- Add SQLite/Postgres sink for historical KPIs

\- Add SMTP / Slack webhooks for `notify`

\- Add PDF via `reportlab` or `weasyprint`

\- Add Docker Compose with inbox watcher

\- Add CI (GitHub Actions) running pytest + coverage gate

\- Add structured JSON logging for log aggregation



\## 8. How to Explain This in an Interview

1\. \*\*Problem:\*\* manual sales reporting is slow and error-prone

2\. \*\*Approach:\*\* ingest → validate → transform → report → notify, scheduled

3\. \*\*Engineering:\*\* config-driven, testable, logged, idempotent

4\. \*\*QA:\*\* unit, integration, performance tests (15 passing)

5\. \*\*Ops:\*\* runbook with cron / Task Scheduler / systemd options

6\. \*\*Result:\*\* reliable, extensible automation a business can actually use

