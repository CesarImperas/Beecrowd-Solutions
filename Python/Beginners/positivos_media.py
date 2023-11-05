# Caio Cesar 25/9/23
# BEE 1064

cont = 0
soma = 0
positivos = 0

while cont < 6:
    cont += 1
    entrada = float(input())
    if entrada > 0:
        soma += entrada
        positivos += 1

media = soma / positivos

print(f'{positivos} valores positivos')
print(f'{media:.1f}')
