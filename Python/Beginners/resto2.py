# Caio Cesar 04/10/23
# BEE 1075

valor = int(input())

for num in range(2, 10000):
    if num % valor == 2:
        print(num)