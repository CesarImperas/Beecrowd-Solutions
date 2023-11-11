# Caio Cesar 09/11/23
# BEE 1044

numeros = [int(n) for n in input().split()]

if numeros[0] % numeros[1] == 0 or numeros[1] % numeros[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')