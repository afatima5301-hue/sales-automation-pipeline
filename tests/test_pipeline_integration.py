from pathlib import Path
import yaml
from src.sales_pipeline.pipeline import run_pipeline


def _write_cfg(tmp_path, sample_df):
    inbox = tmp_path / "inbox"
    inbox.mkdir()
    sample_df.to_csv(inbox / "sales1.csv", index=False)

    cfg = {
        "paths": {
            "inbox": str(inbox),
            "processed": str(tmp_path / "processed"),
            "archive": str(tmp_path / "archive"),
            "reports": str(tmp_path / "reports"),
            "logs": str(tmp_path / "logs"),
        },
        "validation": {
            "required_columns": ["order_id","order_date","region","product","quantity","unit_price"],
            "max_null_fraction": 0.2,
            "min_quantity": 1,
            "max_unit_price": 100000,
        },
        "notification": {"channel": "console"},
        "schedule": {"enabled": False, "cron": "0 7 * * *"},
    }
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg))
    return str(cfg_path), inbox


def test_end_to_end(sample_df, tmp_path):
    cfg_path, inbox = _write_cfg(tmp_path, sample_df)
    result = run_pipeline(cfg_path)

    assert result["files"] == 1
    assert result["rows"] == 3
    assert Path(result["report"]).exists()
    assert not list(inbox.glob("*.csv"))
    assert list((tmp_path / "archive").glob("*.csv"))


def test_bad_file_is_skipped(sample_df, tmp_path):
    cfg_path, inbox = _write_cfg(tmp_path, sample_df)
    (inbox / "bad.csv").write_text("not,a,valid,csv\n1,2,3")

    result = run_pipeline(cfg_path)
    assert result["files"] == 1
    assert any("bad.csv" in name for name, _ in result["failed"])