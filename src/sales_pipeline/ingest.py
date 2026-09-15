from pathlib import Path
import pandas as pd


def list_inbox_files(inbox: str) -> list[Path]:
    '''Return all CSV files in inbox, sorted by name.'''
    return sorted(Path(inbox).glob('*.csv'))


def read_csv_safe(path: Path) -> pd.DataFrame:
    '''Read a CSV with a friendly error if something is wrong.'''
    try:
        df = pd.read_csv(path)
    except Exception as e:
        raise ValueError(f'Failed to read {path.name}: {e}') from e

    df['__source_file'] = path.name
    return df
