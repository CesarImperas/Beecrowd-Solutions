# Caio Cesar 25/10/23
# BEE 1146

while True:
    numero = int(input())
    if numero == 0: break

    for num in range(1, numero + 1):
        if num == numero:
            print(num)
        else:
            print(f'{num} ', end='')