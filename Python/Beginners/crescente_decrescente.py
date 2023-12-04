# Caio Cesar 01/12/23
# BEE 1113

while True:
    numeros  = input().split()
    num_x = int(numeros[0])
    num_y = int(numeros[1])

    if num_x > num_y:
        print("Decrescente")
    elif num_x < num_y:
        print("Crescente")
    else:
        break