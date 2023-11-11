# Caio Cesar 09/11/23
# BEE 1041

entrada = [float(n) for n in input().split()]

eixo_x = entrada[0]
eixo_y = entrada[1]

if eixo_x == 0 and eixo_y == 0:
    saida = 'Origem'
elif (eixo_x == 0 and eixo_y > 0) or (eixo_x == 0 and eixo_y < 0):
    saida = 'Eixo Y'
elif (eixo_y == 0 and eixo_x > 0) or (eixo_y == 0 and eixo_x < 0):
    saida = 'Eixo X'
elif eixo_x > 0 and eixo_y > 0:
    saida = 'Q1'
elif eixo_x < 0 and eixo_y > 0:
    saida = 'Q2'
elif eixo_x < 0 and eixo_y < 0:
    saida = 'Q3'
elif eixo_x > 0 and eixo_y < 0:
    saida = 'Q4'

print(saida)  