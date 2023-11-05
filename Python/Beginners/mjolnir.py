# Caio Cesar 25/9/23
# BEE 1865

contador = int(input())

while contador > 0:
    contador -= 1
    entrada = input().split()
    if entrada[0] in 'Thor':
        print('Y')
    else:
        print('N')