# Caio Cesar 27/10/23
# BEE 2344

nota = int(input())

if nota == 0:
    print('E')
elif 1 <= nota <= 35:
    print('D')
elif 36 <= nota <= 60:
    print('C')
elif 61 <= nota <= 85:
    print('B')
elif 86 <= nota <= 100:
    print('A')