# Caio Cesar 10/12/23
# BEE 1183

operacao = input().upper()

matriz = [12 * [0] for i in range(12)]
soma = 0

for linha in range(12):
    for coluna in range(12):
        matriz[linha][coluna] = float(input())
        if linha > coluna:
            soma += matriz[linha][coluna]
        
if operacao == 'M':
    media = soma / 66
    print(f"{media:.1f}")
else:
    print(f"{soma:.1f}")
