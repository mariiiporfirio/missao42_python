#!/usr/bin/env python3
import sys, re

word = "Hello"

if len(sys.argv) != 2:
    print("None")
elif len(sys.argv) == 2:
    finder = re.findall(rf"\b\w*{sys.argv[1]}\b",word,re.IGNORECASE)
    if len(finder) > 0:
        print(f"Qual foi o parametro ? {sys.argv[1]}\nBom trabalho !")
    elif len(finder) == 0:
        print(f"Qual foi o parametro ? {sys.argv[1]}\nNão é isso, desculpa...")