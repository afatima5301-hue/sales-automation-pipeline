import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    '''Clean and enrich the dataframe.'''
    df = df.copy()
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df = df.dropna(subset=['order_date'])
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0.0)
    df['revenue'] = df['quantity'] * df['unit_price']
    df['region'] = df['region'].astype(str).str.strip().str.title()
    df['product'] = df['product'].astype(str).str.strip()
    return df


def kpis(df: pd.DataFrame) -> dict:
    '''Compute key performance indicators.'''
    if df.empty:
        return {
            'total_revenue': 0.0,
            'total_orders': 0,
            'top_products': [],
            'by_region': {},
        }

    by_region = df.groupby('region')['revenue'].sum().round(2).to_dict()

    top_products = (
        df.groupby('product')['revenue']
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .round(2)
        .to_dict()
    )

    return {
        'total_revenue': round(float(df['revenue'].sum()), 2),
        'total_orders': int(df['order_id'].nunique()),
        'top_products': top_products,
        'by_region': by_region,
    }
