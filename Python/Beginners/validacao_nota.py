# Caio Cesar 01/12/23
# BEE 1117

contador = 0
soma = 0
while contador < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        contador += 1
        soma += nota
    else:
        print("nota invalida")

media = soma / 2

print(f"media = {media:.2f}")