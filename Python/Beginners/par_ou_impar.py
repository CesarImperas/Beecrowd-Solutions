# Caio Cesar 10/11/23
# BEE 1074

teste = int(input())

for i in range(teste):
    num = int(input())

    if num == 0:
        print('NULL')
    elif num < 0 and num % 2 == 0:
        print('EVEN NEGATIVE')
    elif num < 0 and num % 2 != 0:
        print('ODD NEGATIVE')
    elif num > 0 and num % 2 == 0:
        print('EVEN POSITIVE')
    elif num > 0 and num % 2 != 0:
        print('ODD POSITIVE')