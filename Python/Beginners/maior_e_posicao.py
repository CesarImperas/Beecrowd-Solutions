# Caio Cesar 02/11/23
# BEE 1080

lista = []
for i in range(100):
    entrada = int(input())
    lista.append(entrada)

maior = lista[0]
posicao = 0
for j in range(len(lista)):
    if lista[j] > maior:
        maior = lista[j]
        posicao = j + 1

print(maior)
print(posicao)