#!/usr/bin/env python3

usu_input = str(input("Como posso ajudar ? "))
stop = "stop"

while usu_input.lower() != stop:
    usu_input = str((input("Entendi, algo mais ? ")))
    if usu_input.lower() == stop:
        break