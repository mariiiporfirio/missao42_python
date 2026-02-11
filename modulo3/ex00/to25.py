#!/usr/bin/env python3

usu_num = int(input("Informe um número menor que 25: "))
x = 1

if usu_num >= 26:
    print("Error")

while usu_num <= 25:
    print(f"Dentro do loop, minha variável é {usu_num}")
    usu_num += 1