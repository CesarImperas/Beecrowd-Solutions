# Caio Cesar 06/11/23
# BEE 2311

def min_max(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    
    menor = lista[0]
    for j in range(len(lista)):
        if lista[j] < menor:
            menor = lista[j]

    return (maior, menor)


competidores = int(input())

for i in range(competidores):
    nome = input()
    grau = float(input())
    notas = [float(n) for n in input().split()]

    maior_e_menor = min_max(notas)

    notas.remove(maior_e_menor[0])
    notas.remove(maior_e_menor[1])

    soma = sum(notas)

    nota_final = soma * grau

    print(f'{nome} {nota_final:.2f}')