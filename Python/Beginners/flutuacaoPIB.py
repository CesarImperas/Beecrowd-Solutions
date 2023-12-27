# Caio Cesar 25/12/23
# BEE 3346
# Taxa de juros acumulada

entrada = input().split()

f1 = float(entrada[0])
f2 = float(entrada[1])

flutuacao = (((1 + (f1/100)) * (1 + (f2/100))) - 1) * 100

print(f"{flutuacao:.6f}")