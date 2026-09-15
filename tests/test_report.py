from src.sales_pipeline.transform import clean, kpis
from src.sales_pipeline.report import write_excel, write_summary_csv


def test_write_excel(sample_df, tmp_path):
    df = clean(sample_df)
    path = write_excel(df, kpis(df), str(tmp_path))
    assert path.exists()
    assert path.suffix == ".xlsx"


def test_write_csv(sample_df, tmp_path):
    df = clean(sample_df)
    path = write_summary_csv(kpis(df), str(tmp_path))
    assert path.exists()
    assert path.suffix == ".csv"