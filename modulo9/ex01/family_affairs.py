#!/usr/bin/env python3

def find_the_redheads(família_dupont):

    lista = []

    for nome in filter(lambda n: família_dupont[n] == "red", família_dupont.keys()):
        lista.append(nome)
    
    return lista

família_dupont = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(família_dupont))