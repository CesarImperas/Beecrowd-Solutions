# Caio Cesar 23/10/23
# BEE 2167

testes = int(input())

casos = [int(n) for n in input().split()]

indice = 0
for i in range(1, len(casos)):
    if casos[i-1] > casos[i]:
        indice = i + 1
        break
print(indice)
