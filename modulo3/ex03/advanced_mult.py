#!/usr/bin/env python3

y = 0

while y <= 10:
    print(f"Tabuada do {y}: ", end="")
    x = 0
    while x <= 10:
        result = y * x
        print(f"{result} ", end="")
        x += 1
    y += 1
    print()