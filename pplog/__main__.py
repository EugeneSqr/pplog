import sys
import signal

from parser import parse_log_entry
from transformer import transform
from pprinter import pprint

signal.signal(signal.SIGINT, lambda _, __: sys.exit(0))

for line in sys.stdin:
    query = sys.argv[1] if len(sys.argv) > 1 else ''
    for block in parse_log_entry(line):
        transformed = transform(block.parsed, query)
        line = line.replace(block.raw, pprint(transformed))
    sys.stdout.write(line)
