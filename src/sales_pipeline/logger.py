import logging
from pathlib import Path


def get_logger(name: str = 'pipeline', log_dir: str = 'logs') -> logging.Logger:
    '''Return a logger that writes to both console and file.'''
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    fmt = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

    fh = logging.FileHandler(Path(log_dir) / 'pipeline.log', encoding='utf-8')
    fh.setFormatter(fmt)

    sh = logging.StreamHandler()
    sh.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger
