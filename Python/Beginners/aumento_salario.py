# Caio Cesar 09/11/23
# BEE 1048

salario = float(input())

if 0 <= salario <= 400:
    porcentagem = 0.15
elif 400.01 <= salario <= 800:
    porcentagem = 0.12
elif 800.01 <= salario <= 1200:
    porcentagem = 0.10
elif 1200.01 <= salario <= 2000:
    porcentagem = 0.07
else:
    porcentagem = 0.04

reajuste = porcentagem * salario
novo_salario = reajuste + salario

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {porcentagem*100:.0f} %')