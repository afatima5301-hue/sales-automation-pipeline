import time
import pandas as pd

from src.sales_pipeline.transform import clean, kpis


def test_large_dataset_performance():
    n = 100_000
    df = pd.DataFrame({
        "order_id": range(n),
        "order_date": ["2024-01-01"] * n,
        "region": ["north"] * n,
        "product": ["Widget"] * n,
        "quantity": [2] * n,
        "unit_price": [10.0] * n,
    })

    start = time.perf_counter()
    cleaned = clean(df)
    _ = kpis(cleaned)
    elapsed = time.perf_counter() - start

    assert elapsed < 5.0, f"Transform too slow: {elapsed:.2f}s"