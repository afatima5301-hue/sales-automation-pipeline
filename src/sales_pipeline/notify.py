from pathlib import Path
from datetime import datetime


def notify(message: str, channel: str = 'console', file_path: str | None = None) -> None:
    '''Send a notification to console or a file.'''
    stamp = datetime.now().isoformat(timespec='seconds')
    line = f'[{stamp}] {message}'

    if channel == 'console':
        print(line)
    elif channel == 'file':
        if not file_path:
            raise ValueError('file_path required for file channel')
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(line + '\n')
    else:
        raise ValueError(f'Unsupported channel: {channel}')
