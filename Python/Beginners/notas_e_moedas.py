# Caio Cesar 12/11/23
# BEE 1021

dinheiro = float(input())

#-------------------------NOTAS---------------------------------------------------
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

#-------------------------MOEDAS---------------------------------------------------

moeda1 = round(dinheiro // 1, 2)
dinheiro = round(dinheiro % 1, 2)

moeda50 = round(dinheiro // 0.5, 2)
dinheiro = round(dinheiro % 0.5, 2)

moeda25 = round(dinheiro // 0.25, 2)
dinheiro = round(dinheiro % 0.25, 2)

moeda10 = round(dinheiro // 0.1, 2)
dinheiro = round(dinheiro % 0.1, 2)

moeda05 = round(dinheiro // 0.05, 2)
dinheiro = round(dinheiro % 0.05, 2)

moeda01 = round(dinheiro * 100, 2)

#----------------------------------------------------------------------------------

print('NOTAS:')
print(f'{int(nota100)} nota(s) de R$ 100.00')
print(f'{int(nota50)} nota(s) de R$ 50.00')
print(f'{int(nota20)} nota(s) de R$ 20.00')
print(f'{int(nota10)} nota(s) de R$ 10.00')
print(f'{int(nota5)} nota(s) de R$ 5.00')
print(f'{int(nota2)} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{int(moeda1)} moeda(s) de R$ 1.00')
print(f'{int(moeda50)} moeda(s) de R$ 0.50')
print(f'{int(moeda25)} moeda(s) de R$ 0.25')
print(f'{int(moeda10)} moeda(s) de R$ 0.10')
print(f'{int(moeda05)} moeda(s) de R$ 0.05')
print(f'{int(moeda01)} moeda(s) de R$ 0.01')