#!/usr/bin/env python3

def add_one(n: int):
    x = n + 1
    print(f"Variável alterada:{x}")

result = 7
print(f"Variável original: {result}")

add_one(result)
print(f"Variável pós função: {result}")
