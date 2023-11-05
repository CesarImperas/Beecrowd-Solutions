# Caio Cesar 14/9/23
# BEE 1061

entrada1_1 = input().split()
dia1 = int(entrada1_1[1])

entrada1_2 = input().split(' : ')
horas1 = int(entrada1_2[0]) 
minutos1 = int(entrada1_2[1])
segundos1 = int(entrada1_2[2]) 

entrada2_1 = input().split()
dia2 = int(entrada2_1[1])

entrada2_2 = input().split(' : ')
horas2 = int(entrada2_2[0])
minutos2 = int(entrada2_2[1])
segundos2 = int(entrada2_2[2])

tempo1 = (dia1*86400)+(horas1*3600)+(minutos1*60)+(segundos1)
tempo2 = (dia2*86400)+(horas2*3600)+(minutos2*60)+(segundos2)

tempo_total = tempo2 - tempo1

dias_total = tempo_total // 86400
tempo_total %= 86400

horas_total = tempo_total // 3600
tempo_total %= 3600

minutos_total = tempo_total // 60
tempo_total %= 60

segundos_total = tempo_total

print(f'{dias_total} dia(s)')
print(f'{horas_total} hora(s)')
print(f'{minutos_total} minuto(s)')
print(f'{segundos_total} segundo(s)')