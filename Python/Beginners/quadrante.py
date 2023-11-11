# Caio Cesar 09/11/23
# BEE 1115

while True:
    entrada = [int(n) for n in input().split()]

    par_x = entrada[0]
    par_y = entrada[1]

    if par_x == 0 or par_y == 0: break

    if par_x > 0 and par_y > 0:
        print('primeiro')
    elif par_x < 0 and par_y > 0:
        print('segundo')
    elif par_x < 0 and par_y < 0:
        print('terceiro')
    elif par_x > 0 and par_y < 0:
        print('quarto')