# Caio Cesar 24/9/23
# BEE 1042

entrada = input().split()

numeros = []
for i in entrada:
    num = int(i)
    numeros.append(num)

ordenados = sorted(numeros) # Para variável, precisa inserir uma função, e não método, como o .sort()

for j in ordenados:
    print(j)

print()

for k in entrada:
    print(k)