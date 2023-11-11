# Caio Cesar 09/11/23
# BEE 1116

testes = int(input())

for i in range(testes):
    entrada = [int(n) for n in input().split()]
    num1 = entrada[0]
    num2 = entrada[1]

    if num2 == 0:
        print('divisao impossivel')
    else:
        divisao = num1/num2
        print(f'{divisao:.1f}')