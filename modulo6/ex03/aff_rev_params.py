#!/usr/bin/env python3
import sys

x = 1
y = 0
list = []

if len(sys.argv) < 3:
    print("None")
elif len(sys.argv) >= 3:
    while x < len(sys.argv):
        list.append(sys.argv[x])
        x +=1
    list.reverse()

    while y < len(list):
        print(f"{list[y]}")
        y += 1