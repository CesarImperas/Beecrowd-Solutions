# Caio Cesar 02/12/23
# BEE 1134

alcool = 0
diesel = 0
gasolina = 0

while True:
    entrada = int(input())
    if 1 <= entrada < 4:
        if entrada == 1:
            alcool += 1
        elif entrada == 2:
            gasolina += 1
        else:
            diesel += 1
    elif entrada == 4: break

print(f"MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")

