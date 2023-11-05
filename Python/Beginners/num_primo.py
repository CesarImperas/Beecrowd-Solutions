# Caio Cesar 17/9/23
# BEE 1165

testes = int(input())

for i in range(testes):
    num = int(input())

    primo = True

    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            primo = False
            break
    if primo:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')