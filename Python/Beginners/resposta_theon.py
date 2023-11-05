# Caio Cesar 25/9/23
# BEE 1858

contador = int(input())

valores = [int(n) for n in input().split()]

maximo = 20
posicao = 0

for i,num in enumerate(valores):
    if num < maximo:
        maximo = num
        posicao = i + 1

print(posicao)



