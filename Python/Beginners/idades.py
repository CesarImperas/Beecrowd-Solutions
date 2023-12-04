# Caio Cesar 02/12/23
# BEE 1154

soma = 0
qntd = 0
while True:
    idade = int(input())
    if idade < 0: break
    soma += idade
    qntd += 1

media = soma / qntd

print(f"{media:.2f}")