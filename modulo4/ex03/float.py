#!/usr/bin/env python3

usu_num = input("Informe um número: ")
usu_convert = float(usu_num)

if usu_convert.is_integer():
    print("Este número é um inteiro.")
else:
    print("Este número é um decimal.")