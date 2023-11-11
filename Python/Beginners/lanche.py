# Caio Cesar 09/11/23
# BEE 1038

codigos = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

entrada = [int(n) for n in input().split()]

valor = codigos[entrada[0]] * entrada[1]

print(f'Total: R$ {valor:.2f}')