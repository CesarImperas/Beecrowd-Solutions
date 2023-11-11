# Caio Cesar 09/11/23
# BEE 1177

num_t = int(input())

contador = 0
for i in range(1000):
    print(f'N[{i}] = {contador}')
    
    contador += 1
    if contador == num_t:
        contador = 0