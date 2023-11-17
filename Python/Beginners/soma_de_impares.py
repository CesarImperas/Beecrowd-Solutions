# Caio Cesar 12/11/23
# BEE 1071

num_x = int(input())
num_y = int(input())

soma = 0
for n in range(num_y + 1, num_x):
    if n % 2 != 0:
        soma += n

print(soma)