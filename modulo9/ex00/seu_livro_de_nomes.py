#!/usr/bin/env python3

def array_de_nomes(pessoas):

    lista = []

    for nome, sobrenome in pessoas.items():
        full = nome.capitalize() + " " + sobrenome.capitalize()
        lista.append(full)
    
    return lista

pessoas = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
    }

print(array_de_nomes(pessoas))