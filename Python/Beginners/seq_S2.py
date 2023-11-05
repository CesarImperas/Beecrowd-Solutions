# Caio Cesar 04/11/23
# BEE 1156

numerador = 1
denominador = 1
soma = 0
while numerador <= 39:
    soma += numerador/denominador
    numerador += 2
    denominador *= 2

print(f'{soma:.2f}')