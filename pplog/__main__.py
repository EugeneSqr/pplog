import sys
import signal

import pprint_blocks
from pprinter import pprint

for line in sys.stdin:
    signal.signal(signal.SIGINT, lambda _, __: sys.exit(0))
    query = sys.argv[1] if len(sys.argv) > 1 else ''
    for block in pprint_blocks.get(line):
        transformed = pprint_blocks.transform(block.parsed, query)
        line = line.replace(block.raw, pprint(transformed))
    sys.stdout.write(line)
