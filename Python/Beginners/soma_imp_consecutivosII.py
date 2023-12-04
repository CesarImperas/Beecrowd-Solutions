# Caio Cesar 01/12/23
# BEE 1099

casos = int(input())

for i in range(casos):
    numeros = input().split()
    num_x = int(numeros[0])
    num_y = int(numeros[1])

    soma = 0
    if num_x > num_y:
        for n in range(num_y + 1, num_x):
            if n % 2 != 0:
                soma += n
    elif num_y > num_x:
        for n in range(num_x + 1, num_y):
            if n % 2 != 0:
                soma += n
    
    print(soma)