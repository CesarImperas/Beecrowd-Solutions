# Caio Cesar 02/12/23
# BEE 1158

casos = int(input())

for i in range(casos):
    entrada = input().split()
    num = int(entrada[0])
    qntd = int(entrada[1])

    soma = 0
    while qntd > 0:
        if num % 2 != 0:
            soma += num
            qntd -= 1
        num += 1

    print(soma)