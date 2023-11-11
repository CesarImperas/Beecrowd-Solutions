# Caio Cesar 10/11/23
# BEE 1070

numero = int(input())

contador = 0
while contador < 6:
    if numero % 2 != 0:
        print(numero)
        contador += 1
    numero += 1