# Caio Cesar 25/9/23
# BEE 1564

while True:
    try:
        entrada = input()
        if int(entrada) > 0:    
            print('vai ter duas!')
        else:
            print('vai ter copa!')
    except EOFError: break