# Caio Cesar 25/9/23
# BEE 2006

cha_real = input()

entrada = input().split()

contador = 0
for i,cha in enumerate(entrada):
    if cha == cha_real:
        contador += 1

print(contador)
    