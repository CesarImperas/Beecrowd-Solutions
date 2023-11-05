# Caio Cesar 04/10/23
# BEE 1133

valor_x = int(input())
valor_y = int(input())
lista = sorted([valor_x, valor_y])

for num in range(lista[0] + 1, lista[1]):
    if num % 5 == 2 or num % 5 == 3:
        print(num)
