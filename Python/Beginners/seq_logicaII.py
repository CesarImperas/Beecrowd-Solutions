# Caio Cesar 02/12/23
# BEE 1145

valores = input().split()

valor_x = int(valores[0])
valor_y = int(valores[1])

x = 1

for y in range(1, valor_y + 1):
    if x == valor_x:
        print(y)
        x = 1
    else:
        print(y, end= " ")
        x += 1