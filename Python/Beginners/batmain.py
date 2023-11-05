# Caio Cesar 22/10/23
# BEE 2510

teste = int(input())

for i in range(teste):
    nome = str(input())
    if nome.lower() != "batmain" and nome.lower() != "batman":
        print("Y")
    else:
        print("N")