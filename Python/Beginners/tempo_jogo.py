# Caio Cesar 12/11/23
# BEE 1046

entrada = input().split()

hora_ini = int(entrada[0])
hora_fim = int(entrada[1])

if hora_ini >= hora_fim:
    tempo = 24 - hora_ini + hora_fim
    print(f'O JOGO DUROU {tempo} HORA(S)')
else:
    tempo = hora_fim - hora_ini
    print(f'O JOGO DUROU {tempo} HORA(S)')