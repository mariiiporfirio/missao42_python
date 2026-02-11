#!/usr/bin/env python3

password = 1234

usu_password = int(input("Digite a senha numérica: "))

if usu_password == password:
    print("ACESSO CONCEDIDO")
elif usu_password != password:
    print("ACESSO NEGADO")