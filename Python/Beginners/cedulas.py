# Caio Cesar 18/11/23
# BEE 1018

dinheiro = int(input())

print(dinheiro)

nota100 = dinheiro // 100
dinheiro = dinheiro % 100

nota50 = dinheiro // 50
dinheiro = dinheiro % 50

nota20 = dinheiro // 20
dinheiro = dinheiro % 20

nota10 = dinheiro // 10
dinheiro = dinheiro % 10

nota5 = dinheiro // 5
dinheiro = dinheiro % 5

nota2 = dinheiro // 2
dinheiro = dinheiro % 2

nota1 = dinheiro // 1
dinheiro = dinheiro % 1

print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")