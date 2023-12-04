# Caio Cesar 02/12/23
# BEE 1175

vetor = []

for i in range(20):
    num = int(input())
    vetor.append(num)

vetor.reverse()

for j in range(20):
    print(f"N[{j}] = {vetor[j]}")
