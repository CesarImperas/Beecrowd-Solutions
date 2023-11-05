# Caio Cesar 25/10/23
# BEE 1962

testes = int(input())

for casos in range(testes):
    ano = int(input())
    if ano >= 2015:
        notacao = 'A.C.'
    else:
        notacao = 'D.C.'
    transcorrido = abs(ano - 2015)
    
    if notacao == 'A.C.':
        transcorrido += 1

    print(f'{transcorrido} {notacao}')