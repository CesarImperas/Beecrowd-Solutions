# Caio Cesar 30/11/23
# BEE 1060

positivos = 0
for i in range(6):
    numero = float(input())
    if numero > 0:
        positivos += 1

print(f"{positivos} valores positivos")