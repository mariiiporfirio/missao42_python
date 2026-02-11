#!/usr/bin/env python3
import sys

def downcase_it(x: str):
    for y in x[1:]:
        print(y.lower())

    if len(x) == 1:
        print("None")


downcase_it(sys.argv)
