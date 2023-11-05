# Caio Cesar 20/9/23
# BEE 1168

limite = int(input())

for i in range(limite):
    entrada = input()
    
    leds = 0

    for i in entrada:
        if i == '0' or i == '6' or i == '9':
            leds += 6
        elif i == '1':
            leds += 2
        elif i == '2' or i == '3' or i == '5':
            leds += 5
        elif i == '4':
            leds += 4
        elif i == '7':
            leds += 3
        elif i == '8':
            leds += 7
    
    print(f'{leds} leds')




