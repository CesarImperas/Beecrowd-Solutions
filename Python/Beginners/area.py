# Caio Cesar
# BEE 1012 

num = input().split()

numA = float(num[0])
numB = float(num[1])
numC = float(num[2])

# a área do triângulo retângulo que tem A por base e C por altura
triangulo = (numA*numC)/2

# a área do círculo de raio C
PI = 3.14159
circulo = PI*(numC**2)

# a área do trapézio que tem A e B por bases e C por altura
trapezio = ((numA+numB)*numC)/2

# a área do quadrado que tem lado B
quadrado = numB**2

# a área do retângulo que tem lados A e B
retangulo = numA*numB

print(f'TRIANGULO: {triangulo:.3f} \nCIRCULO: {circulo:.3f} \nTRAPEZIO: {trapezio:.3f} \nQUADRADO: {quadrado:.3f} \nRETANGULO: {retangulo:.3f}')