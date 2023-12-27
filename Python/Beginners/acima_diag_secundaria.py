# Caio Cesar 22/12/23
# BEE 1185

operacao = input().upper()

matriz = [12 * [0] for i in range(12)]
soma = 0
qntd = 0

for linha in range(12):
    for coluna in range(12):
        matriz[linha][coluna] = float(input())

        if coluna < 11 - linha:
            soma += matriz[linha][coluna]
            qntd += 1

if operacao == 'M':
    media = soma / qntd
    print(f"{media:.1f}")
else:
    print(f"{soma:.1f}")