# Caio Cesar 23/10/23
# BEE 2582

testes = int(input())

for i in range(testes):
    entrada = [int(n) for n in input().split()]
    soma = 0
    for num in entrada:
        soma += num
    if soma == 0:
        print('PROXYCITY')
    elif soma == 1:
        print('P.Y.N.G.')
    elif soma == 2:
        print('DNSUEY!')
    elif soma == 3:
        print('SERVERS')
    elif soma == 4:
        print('HOST!')
    elif soma == 5:
        print('CRIPTONIZE')
    elif soma == 6:
        print('OFFLINE DAY')
    elif soma == 7:
        print('SALT')
    elif soma == 8:
        print('ANSWER!')
    elif soma == 9:
        print('RAR?')
    elif soma == 10:
        print('WIFI ANTENNAS')