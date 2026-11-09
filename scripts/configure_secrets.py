"""Run privately in a real server terminal; never prints or logs keys."""
from pathlib import Path
import getpass
import os
import sys

if not sys.stdin.isatty():
    raise SystemExit('Run this yourself in an interactive terminal. Do not pipe keys.')
root = Path(__file__).resolve().parents[1]
target = root / '.env'
if target.exists():
    raise SystemExit('An environment file already exists. Review it privately before changing it.')
values = {}
for key in ('GROQ_API_KEY', 'JINA_API_KEY'):
    value = getpass.getpass(key + ' (hidden): ').strip()
    if not value or any(c in value for c in '\n\r\x00'):
        raise SystemExit('Invalid empty or multiline key; nothing saved.')
    values[key] = value
fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
with os.fdopen(fd, 'w') as stream:
    for key, value in values.items():
        stream.write(key + '=' + value + '\n')
print('Saved private server-only keys. Do not upload or display this file.')
