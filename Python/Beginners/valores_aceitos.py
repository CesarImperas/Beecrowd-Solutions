# Caio Cesar 
# BEE 1035

num = input().split()

numA = int(num[0])
numB = int(num[1])
numC = int(num[2])
numD = int(num[3])
somaAB = numA+numB
somaCD = numC+numD

if (numB > numC) and (numD > numA) and (somaCD > somaAB) and (numC > 0 and numD > 0) and numA % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')