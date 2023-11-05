# Caio Cesar 17/9/23
# BEE 1047


entrada = input().split()

hr1 = int(entrada[0])
min1 = int(entrada[1])
hr2 = int(entrada[2])
min2 = int(entrada[3])

tempo1 = (hr1*60) + min1
tempo2 = (hr2*60) + min2

tempo_total= tempo2 - tempo1

if tempo_total <= 0:
    tempo_total += 24*60
    
hrtotal = tempo_total // 60
mintotal = tempo_total % 60
    
print(f'O JOGO DUROU {hrtotal} HORA(S) E {mintotal} MINUTO(S)')
