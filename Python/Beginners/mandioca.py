# Caio Cesar 28/10/23
# BEE 2936

soma = 225
for i in range(5):
    porcao = int(input())
    if i == 0:
        soma += (porcao * 300)
    elif i == 1:
        soma += (porcao * 1500)
    elif i == 2:
        soma += (porcao * 600)
    elif i == 3:
        soma += (porcao * 1000)
    else:
        soma += (porcao * 150)
    
print(soma)