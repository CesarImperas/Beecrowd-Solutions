# Caio Cesar 06/11/23
# BEE 1182

coluna = int(input())
operacao = input()


nums_lins = 12
nums_cols = 12

matriz = [[0] * nums_lins for i in range(nums_cols)]
for ilin in range(nums_lins):
    for icol in range(nums_cols):
        matriz[ilin][icol] = float(input()) # type: ignore

soma = 0
for ilin in range(nums_lins):
    soma += matriz[ilin][coluna]

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    media = soma/12
    print(f'{media:.1f}')