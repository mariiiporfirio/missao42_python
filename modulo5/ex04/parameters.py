#!/usr/bin/env python3
import sys
x = 1
new_list = []

while x < len(sys.argv):
    new_list.append(sys.argv[x])
    x += 1

print("Número de parâmetros:", len(new_list))