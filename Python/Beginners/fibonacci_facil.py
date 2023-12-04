# Caio Cesar 02/12/23
# BEE 1151

num_N = int(input())

lista = [0, 1]

while len(lista) < num_N:
    valor1 = lista[-1]
    valor2 = lista[-2]
    lista.append(valor1 + valor2)

for i in range(num_N):
    if i == num_N - 1:
        print(lista[i])
    else:
        print(lista[i], end= " ")