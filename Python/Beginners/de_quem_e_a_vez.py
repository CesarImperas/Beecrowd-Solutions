# Caio Cesar 11/11/23
# BEE 1914

casos = int(input())

for i in range(casos):
    jogadores = input().split()
    valores = [int(n) for n in input().split()]
    soma = valores[0] + valores[1]

    for j in range(1, 4, 2):
        if soma % 2 == 0 and jogadores[j] == 'PAR':
            print(jogadores[j-1])
        elif soma % 2 != 0 and jogadores[j] == 'IMPAR':
            print(jogadores[j-1])