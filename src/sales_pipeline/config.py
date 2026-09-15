from pathlib import Path
import yaml


def load_config(path: str = 'config.yaml') -> dict:
    '''Load YAML config and ensure all path folders exist.'''
    with open(path, 'r', encoding='utf-8') as f:
        cfg = yaml.safe_load(f)

    for key, value in cfg['paths'].items():
        Path(value).mkdir(parents=True, exist_ok=True)

    return cfg
