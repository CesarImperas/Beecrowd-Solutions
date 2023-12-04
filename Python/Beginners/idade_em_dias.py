# Caio Cesar 18/11/23
# BEE 1020

dias = int(input())

aux = dias % 365
anos = dias // 365
meses = aux // 30
dias = aux % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")