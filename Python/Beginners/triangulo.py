# Caio Cesar 10/11/23
# BEE 1043

entrada = [float(n) for n in input().split()]

valor_A = entrada[0]
valor_B = entrada[1]
valor_C = entrada[2]

if (valor_A + valor_B > valor_C) and (valor_A + valor_C > valor_B) and (valor_B + valor_C > valor_A):
    perimetro = valor_A + valor_B + valor_C
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((valor_A + valor_B) * valor_C)/2
    print(f'Area = {area:.1f}')