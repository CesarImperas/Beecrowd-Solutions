# Caio Cesar 09/11/23
# BEE 1179

impar = []
par = []
for i in range(15):
    num = int(input())

    if num % 2 == 0:
        par.append(num)
        if len(par) == 5:
            for j in range(5):
                print(f'par[{j}] = {par[j]}')
            par = []
    else:
        impar.append(num)
        if len(impar) == 5:
            for k in range(5):
                print(f'impar[{k}] = {impar[k]}')
            impar = []

if len(impar) != 0:
    for l in range(len(impar)):
        print(f'impar[{l}] = {impar[l]}')

if len(par) != 0:
    for m in range(len(par)):
        print(f'par[{m}] = {par[m]}')