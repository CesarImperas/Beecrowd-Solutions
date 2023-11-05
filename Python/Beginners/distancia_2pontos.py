# Caio Cesar
# BEE 1015

par1 = input().split()
par2 = input().split()

x1 = float(par1[0])
x2 = float(par2[0])
y1 = float(par1[1])
y2 = float(par2[1])

distancia = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)

print(f'{distancia:.4f}')
