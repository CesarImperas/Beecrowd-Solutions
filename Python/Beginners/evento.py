# Caio Cesar 23/10/23
# BEE 2172

while True:
    entrada = [int(n) for n in input().split()]
    if entrada[0] == 0 and entrada[1] == 0: break

    novo_exp = entrada[0] * entrada[1]
    print(novo_exp)
