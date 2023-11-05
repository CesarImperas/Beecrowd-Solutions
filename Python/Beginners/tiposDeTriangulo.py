# Caio Cesar
# BEE 1045

num = input().split()

num1 = float(num[0])
num2 = float(num[1])
num3 = float(num[2])

# Descobrir o maior lado do triangulo (numA)
if num1 > num2 and num1 > num3:
    numA = num1
    numB = num2
    numC = num3
elif num2 > num1 and num2 > num3:
    numA = num2
    numB = num1
    numC = num3
else:
    numA = num3
    numB = num1
    numC = num2
# Descobrir os tipos do triangulo
if numA >= numB+numC:
    print('NAO FORMA TRIANGULO')
elif (numA**2) == (numB**2)+(numC**2):
    print('TRIANGULO RETANGULO')
elif (numA**2) > (numB**2)+(numC**2):
    print('TRIANGULO OBTUSANGULO')
elif (numA**2) < (numB**2)+(numC**2):
    print('TRIANGULO ACUTANGULO')


if (numA == numB) and (numB == numC) and (numA == numC):
    print('TRIANGULO EQUILATERO')
elif numA == numB or numB == numC:
    print('TRIANGULO ISOSCELES')