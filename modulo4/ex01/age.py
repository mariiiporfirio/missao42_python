#!/usr/bin/env python3

usu_age = input("Qual a sua idade ? ")
usu_convert = int(usu_age)

print(f"Você tem {usu_convert} de idade.")

idade = usu_convert + 30
x = 10

while usu_convert < idade:
    usu_convert = usu_convert + 10
    print(f"Em {x} anos, você terá {usu_convert} de idade.")
    x += 10