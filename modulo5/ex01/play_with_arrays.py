#!/usr/bin/env python3

num = [2,8,9,48,8,22,-12,2]
print(f"Array original: {num}")
num_new = []
x = 0

while x < len(num):
    num_new.append(num[x] + 2)
    x += 1
print(f"Novo array: {num_new}")