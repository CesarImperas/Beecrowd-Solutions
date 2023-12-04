# Caio Cesar 02/12/23
# BEE 1164

casos = int(input())

for i in range(casos):
    num = int(input())
    soma = 0
    for n in range(1, num):
        if n % num == 0 or num % n == 0:
            soma += n
    if soma == num:
        print(f"{num} eh perfeito")
    else:
        print(f"{num} nao eh perfeito")