import pandas as pd

from src.sales_pipeline.transform import clean, kpis


def test_clean_adds_revenue(sample_df):
    out = clean(sample_df)
    assert "revenue" in out.columns
    assert out.loc[0, "revenue"] == 20.0


def test_clean_normalizes_region(sample_df):
    out = clean(sample_df)
    assert set(out["region"]) == {"North", "South"}


def test_kpis(sample_df):
    k = kpis(clean(sample_df))
    assert k["total_orders"] == 3
    assert k["total_revenue"] == 90.0
    assert "Widget" in k["top_products"]


def test_kpis_empty():
    k = kpis(pd.DataFrame(columns=["region","product","revenue","order_id"]))
    assert k["total_revenue"] == 0.0