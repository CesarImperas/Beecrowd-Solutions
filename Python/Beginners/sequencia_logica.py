# Caio Cesar 09/11/23
# BEE 1144

tamanho = int(input())

for i in range(1, tamanho+1):
    quadrado = i**2
    cubo = i**3
    print(f'{i} {quadrado} {cubo}')
    print(f'{i} {quadrado + 1} {cubo + 1}')