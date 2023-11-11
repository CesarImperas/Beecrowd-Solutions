# Caio Cesar 11/11/23
# BEE 2061

entrada = input().split()

abas = int(entrada[0])
acoes = int(entrada[1])

for i in range(acoes):
    acao = input()
    if acao == 'fechou':
        abas += 1
    elif acao == 'clicou':
        abas -= 1

print(abas)