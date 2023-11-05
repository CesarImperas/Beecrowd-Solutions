# Caio Cesar 14/9/23
# BEE 1101

while True:
    par = input().split()
    M = int(par[0])
    N = int(par[1])

    if M <= 0 or N <= 0: break

    menor, maior = 0, 0
    lista = []
    numeros = ''
    soma = 0

    if M > N:
        maior += M
        menor += N
    elif N > M:
        maior += N
        menor += M
    else:
        maior += M
        menor += N

    for consecutivos in range(menor, maior+1):
        lista.append(consecutivos)
        soma += consecutivos

    for i in lista:
        numeros += str(i) + ' '

    print(f'{numeros}Sum={soma}')

