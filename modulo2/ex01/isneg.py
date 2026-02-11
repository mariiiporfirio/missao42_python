#!/usr/bin/env python3

usu_num = int(input("Informe um número: "))

if usu_num == 0:
    print("Este número é positivo e negativo.")
elif usu_num < 0:
    print("Este número é negativo.")
elif usu_num > 0:
    print("Este número é positivo.")