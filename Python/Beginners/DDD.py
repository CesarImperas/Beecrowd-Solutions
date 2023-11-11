# Caio Cesar 09/11/23
# BEE 1050

ddd = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro', 32: 'Juiz de Fora', 19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}

entrada = int(input())

existe = False
for k in ddd.keys():
    if k == entrada:
        existe = True
        print(ddd[k])

if not existe:
    print('DDD nao cadastrado')