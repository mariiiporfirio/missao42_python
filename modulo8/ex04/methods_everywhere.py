#!/usr/bin/env python3
import sys

def shrink(x: str):
    print(x[:8])

def enlarge(x: str):
    print(x + "Z" * (8 - len(x)))

for v in sys.argv[1:]:
    if len(v) == 8:
        print(v)
    elif len(v) > 8:
        shrink(v)
    elif len(v) < 8:
        enlarge(v)
