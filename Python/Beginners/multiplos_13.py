# Caio Cesar 01/12/23
# BEE 1132

num_x = int(input())
num_y = int(input())

soma = 0
if num_x > num_y:
    for n in range(num_y, num_x + 1):
        if n % 13 != 0:
            soma += n
elif num_y > num_x:
    for n in range(num_x, num_y + 1):
        if n % 13 != 0:
            soma += n

print(soma)