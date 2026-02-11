#!/usr/bin/env python3

usu_num = int(input("Informe um número: "))
x = 0

while x <= 10:
    result = usu_num * x
    print(f"{x} x {usu_num} = {result}")
    x += 1