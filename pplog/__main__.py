import sys

import jello

import pprint_blocks

for line in sys.stdin:
    #print('>>', pprint_blocks.get(line))
    print(jello)
    sys.stdout.write(line)
