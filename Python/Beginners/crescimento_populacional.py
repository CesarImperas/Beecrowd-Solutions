# Caio Cesar 26/9/23
# BEE 1160

def crescimento(valores):
    anos = 0
    while valores[0] <= valores[1]:
        valores[0] += (valores[0] * valores[2])//100
        valores[1] += (valores[1] * valores[3])//100
        anos += 1

        if anos > 100: return 'Mais de 1 seculo.'
    return f'{anos} anos.'

casos = int(input())

for i in range(casos):
    valores = [float(n) for n in input().split()]

    anos = crescimento(valores)
    
    print(anos)
