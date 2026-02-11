#!/usr/bin/env python3
import sys, re

if len(sys.argv) < 3 or len(sys.argv) > 3:
    print("None")
elif len(sys.argv) == 3:
    finder = re.findall(rf"\b\w*{sys.argv[1]}\b",sys.argv[2])
    if len(finder) > 0:
        print(len(finder))
    elif len(finder) == 0:
        print("None")