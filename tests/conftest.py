import pandas as pd
import pytest


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "order_id": [1, 2, 3],
        "order_date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "region": ["north", "SOUTH", "North"],
        "product": ["Widget", "Gadget", "Widget"],
        "quantity": [2, 1, 5],
        "unit_price": [10.0, 20.0, 10.0],
    })


@pytest.fixture
def cfg(tmp_path):
    return {
        "paths": {
            "inbox": str(tmp_path / "inbox"),
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