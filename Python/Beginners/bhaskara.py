# Caio Cesar
# BEE 1036

from math import sqrt

# Precisa do split() pois o input irá receber 3 valores numa mesma linha, separados pelo espaço
numeros = input().split()

# Atribuição a variáveis do cálculo e sua devida tipagem, convertendo de string para float
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])

delta = (b**2) - (4*a*c)

# Condição caso delta for negativo (raiz negativa) e o 'a' for igual a 0 (divisão por zero)
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    raiz1 = (-b + sqrt(delta))/(2*a)
    raiz2 = (-b - sqrt(delta))/(2*a)
    print(f'R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}')
