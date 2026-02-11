#!/usr/bin/env python3

usu_num1 = int(input("Informe o primeiro número: "))
usu_num2 = int(input("Informe o primeiro segundo: "))
result = usu_num1 * usu_num2

if result == 0:
    print(f"{usu_num1} x {usu_num2} = {result}\nEste número é zero.")
elif result < 0:
    print(f"{usu_num1} x {usu_num2} = {result}\nEste número é negativo.")
elif result > 0:
    print(f"{usu_num1} x {usu_num2} = {result}\nEste número é positivo.")