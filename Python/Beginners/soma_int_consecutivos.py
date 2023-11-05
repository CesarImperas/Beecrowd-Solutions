# Caio Cesar 03/11/23
# BEE 1149

numeros = [int(n) for n in input().split()]

valor_A = numeros[0]

soma = 0
for i in range(1, len(numeros)):
    valor = numeros[i]
    if valor > 0:
        for num in range(valor_A, valor + valor_A):
            soma += num
            

print(soma)