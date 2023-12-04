# Caio Cesar 02/12/23
# BEE 1159

while True:
    num = int(input())
    if num == 0: break

    soma = 0
    cont = 0
    while cont < 5:
        if num % 2 == 0:
            soma += num
            cont += 1
        num += 1
        
    
    print(soma)