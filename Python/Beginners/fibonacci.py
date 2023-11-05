# Caio Cesar 26/9/23
# BEE 1176

casos = int(input())

for i in range(casos):
    num = int(input())

    vetor = [0] * (num+1)
    
    for cont in range(num):
        cont += 1
        if vetor[1] != 1:
            vetor[1] = 1 
        else:
            vetor[cont] = vetor[cont-1] + vetor[cont-2]
    
    print(f'Fib({num}) = {vetor[num]}')


