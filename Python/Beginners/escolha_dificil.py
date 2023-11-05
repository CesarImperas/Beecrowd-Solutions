# Caio Cesar 04/11/23
# BEE 2702

refeicoes = [int(n) for n in input().split()]
requisitadas = [int(n) for n in input().split()]

contador = 0
for i in range(len(refeicoes)):
    if refeicoes[i] < requisitadas[i]:
        diferenca = requisitadas[i] - requisitadas[i]
        contador += diferenca

print(contador)