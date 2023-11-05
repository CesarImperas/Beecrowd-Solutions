# Caio Cesar 26/9/23
# BEE 1789

while True:
    try:
        num_lesma = int(input())
        velocidade = [int(n) for n in input().split()]

        lesma_max = max(velocidade)

        if lesma_max < 10:
            print('1')
        elif 10 <= lesma_max < 20:
            print('2')
        elif lesma_max >= 20:
            print('3')
            
    except EOFError: break