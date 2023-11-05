# Caio Cesar 23/10/23
# BEE 2543

while True:
    try:
        entrada = input().split()

        contador = 0
        for i in range(int(entrada[0])):
            casos = input().split()
            if casos[0] == entrada[1] and casos[1] == '0':
                contador += 1

        print(contador)
    except EOFError: break