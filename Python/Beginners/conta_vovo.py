# Caio Cesar 28/10/23
# BEE 2434

entrada = [int(n) for n in input().split()]

menor = entrada[1]
soma = entrada[1]
for i in range(entrada[0]):
    valor = int(input())
    soma += valor
    if menor > soma:
        menor = soma

print(menor)