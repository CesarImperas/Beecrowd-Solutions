# Caio Cesar 02/12/23
# BEE 1150

num_x = int(input())
num_z = int(input())

while num_x >= num_z:
    num_z = int(input())

soma = 0
cont = 0
while soma < num_z:
    soma += num_x
    num_x += 1
    cont += 1

print(cont)