from pathlib import Path
from datetime import datetime
import pandas as pd


def _stamp() -> str:
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def write_excel(df: pd.DataFrame, kpi: dict, out_dir: str) -> Path:
    out = Path(out_dir) / f'sales_report_{_stamp()}.xlsx'
    with pd.ExcelWriter(out, engine='openpyxl') as writer:
        pd.DataFrame([{
            'total_revenue': kpi['total_revenue'],
            'total_orders': kpi['total_orders'],
        }]).to_excel(writer, sheet_name='KPIs', index=False)

        df.to_excel(writer, sheet_name='Data', index=False)

        if kpi['by_region']:
            pd.Series(kpi['by_region']).to_frame('revenue').to_excel(writer, sheet_name='ByRegion')

        if kpi['top_products']:
            pd.Series(kpi['top_products']).to_frame('revenue').to_excel(writer, sheet_name='TopProducts')

    return out


def write_summary_csv(kpi: dict, out_dir: str) -> Path:
    out = Path(out_dir) / f'kpi_summary_{_stamp()}.csv'
    pd.DataFrame([{
        'total_revenue': kpi['total_revenue'],
        'total_orders': kpi['total_orders'],
        'top_product': next(iter(kpi['top_products']), None),
    }]).to_csv(out, index=False)
    return out
