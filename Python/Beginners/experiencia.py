# Caio Cesar 02/12/23
# BEE 1094

casos = int(input())

total = 0
coelhos = 0
ratos = 0
sapos = 0
for i in range(casos):
    entrada = input().split()
    qntd = int(entrada[0])
    
    if entrada[1] == 'C':
        coelhos += qntd
    elif entrada[1] == 'R':
        ratos +=  qntd
    elif entrada[1] == 'S':
        sapos += qntd
    
    total += qntd

por100_coelhos = (coelhos / total) * 100
por100_ratos = (ratos / total) * 100
por100_sapos = (sapos / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {por100_coelhos:.2f} %")
print(f"Percentual de ratos: {por100_ratos:.2f} %")
print(f"Percentual de sapos: {por100_sapos:.2f} %")