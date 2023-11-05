# Caio Cesar 24/9/23
# BEE 1072

contador = int(input())

dentro = 0
fora = 0

while contador > 0:
    contador -= 1
    num = int(input())
    if 10 <= num <= 20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} out')


