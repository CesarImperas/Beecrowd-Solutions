# Caio Cesar 23/10/23
# BEE 1930

tomadas = [int(n) for n in input().split()]

soma = 0
for i in range(len(tomadas)):
    if i == len(tomadas) - 1:
        soma += tomadas[i]
    else:
        soma += tomadas[i] - 1

print(soma)