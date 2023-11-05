# Caio Cesar 02/11/23
# BEE 1180

vetor = int(input())

lista = [int(n) for n in input().split()]

menor = lista[0]
posicao = 0

for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')