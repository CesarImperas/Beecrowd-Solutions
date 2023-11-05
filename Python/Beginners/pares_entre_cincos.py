# Caio Cesar 02/11/23
# BEE 1065

contador = 0
for i in range(5):
    numero = int(input())
    if numero % 2 == 0:
        contador += 1

print(f'{contador} valores pares')