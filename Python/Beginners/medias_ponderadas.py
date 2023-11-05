# Caio Cesar 02/11/23
# BEE 1079

testes = int(input())

for i in range(testes):
    numeros = [float(n) for n in input().split()]
    media_pond = ((numeros[0] * 2) + (numeros[1] * 3) + (numeros[2] * 5))/ 10
    print(f'{media_pond:.1f}')