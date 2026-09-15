from pathlib import Path
import shutil
import time
import pandas as pd

from .config import load_config
from .logger import get_logger
from .ingest import list_inbox_files, read_csv_safe
from .validate import validate, ValidationError
from .transform import clean, kpis
from .report import write_excel, write_summary_csv
from .notify import notify


def run_pipeline(cfg_path: str = "config.yaml") -> dict:
    cfg = load_config(cfg_path)
    log = get_logger(log_dir=cfg["paths"]["logs"])
    start = time.perf_counter()

    files = list_inbox_files(cfg["paths"]["inbox"])
    if not files:
        log.info("No files found in inbox. Nothing to process.")
        return {"files": 0, "rows": 0, "report": None}

    frames, processed, failed = [], [], []

    for f in files:
        try:
            df = read_csv_safe(f)
            validate(df, cfg)
            frames.append(df)
            processed.append(f)
            log.info("Processed %s (%d rows)", f.name, len(df))
        except (ValidationError, ValueError) as e:
            failed.append((f.name, str(e)))
            log.warning("Skipped %s: %s", f.name, e)

    if not frames:
        log.error("All files failed validation.")
        return {"files": 0, "rows": 0, "report": None, "failed": failed}

    combined = pd.concat(frames, ignore_index=True)
    cleaned = clean(combined)
    kpi = kpis(cleaned)

    excel_path = write_excel(cleaned, kpi, cfg["paths"]["reports"])
    csv_path = write_summary_csv(kpi, cfg["paths"]["reports"])

    for f in processed:
        shutil.move(str(f), Path(cfg["paths"]["archive"]) / f.name)

    n = cfg["notification"]
    msg = (f"Pipeline complete | files={len(processed)} rows={len(cleaned)} "
           f"revenue={kpi['total_revenue']} report={excel_path.name}")
    notify(msg, n["channel"], n.get("file_path"))

    elapsed = round(time.perf_counter() - start, 3)
    log.info("Done in %ss. Report: %s | Summary: %s", elapsed, excel_path, csv_path)

    return {
        "files": len(processed),
        "rows": len(cleaned),
        "report": str(excel_path),
        "summary": str(csv_path),
        "kpis": kpi,
        "failed": failed,
        "elapsed_s": elapsed,
    }