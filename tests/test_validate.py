import pandas as pd
import pytest

from src.sales_pipeline.validate import (
    validate, validate_schema, validate_nulls, validate_values, ValidationError
)


def test_schema_ok(sample_df):
    validate_schema(sample_df)


def test_schema_missing():
    with pytest.raises(ValidationError):
        validate_schema(pd.DataFrame({"a": [1]}))


def test_nulls_threshold(sample_df):
    df = sample_df.copy()
    df.loc[0, "region"] = None
    with pytest.raises(ValidationError):
        validate_nulls(df, max_null_fraction=0.1)


def test_negative_quantity(sample_df):
    df = sample_df.copy()
    df.loc[0, "quantity"] = -1
    with pytest.raises(ValidationError):
        validate_values(df)


def test_price_cap(sample_df):
    df = sample_df.copy()
    df.loc[0, "unit_price"] = 10_000_000
    with pytest.raises(ValidationError):
        validate_values(df)


def test_validate_full(sample_df, cfg):
    validate(sample_df, cfg)