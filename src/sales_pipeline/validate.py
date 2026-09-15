import pandas as pd


class ValidationError(Exception):
    '''Raised when data fails a validation rule.'''
    pass


REQUIRED = ['order_id', 'order_date', 'region', 'product', 'quantity', 'unit_price']


def validate_schema(df: pd.DataFrame, required: list[str] | None = None) -> None:
    required = required or REQUIRED
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValidationError(f'Missing required columns: {missing}')


def validate_nulls(df: pd.DataFrame, max_null_fraction: float = 0.2) -> None:
    frac = df.isna().mean()
    bad = frac[frac > max_null_fraction]
    if not bad.empty:
        raise ValidationError(f'Columns exceed null threshold: {bad.to_dict()}')


def validate_values(df: pd.DataFrame, min_quantity: int = 1, max_unit_price: float = 100000) -> None:
    if (df['quantity'] < min_quantity).any():
        raise ValidationError('Found rows with quantity below minimum.')
    if (df['unit_price'] > max_unit_price).any():
        raise ValidationError('Found rows with unit_price above maximum.')
    if (df['unit_price'] < 0).any():
        raise ValidationError('Negative unit_price detected.')


def validate(df: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    v = cfg['validation']
    validate_schema(df, v['required_columns'])
    validate_nulls(df, v['max_null_fraction'])
    validate_values(df, v['min_quantity'], v['max_unit_price'])
    return df
