# Caio Cesar 28/10/23
# BEE 2339

folhas = [int(n) for n in input().split()]

necessita = folhas[0] * folhas[2]
quantidade = folhas[1]

if necessita <= quantidade:
    print('S')
else:
    print('N')