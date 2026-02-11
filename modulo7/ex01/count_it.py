#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if len(sys.argv) < 2:
    print("None")
else:
    print(f"Parâmetros: {len(sys.argv) - 1}")
    for x in sys.argv[1:]:
        print(f"{x}: {len(x)}")
