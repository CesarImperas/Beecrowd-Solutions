# Caio Cesar 02/12/23
# BEE 1118

def calcula_media():
    soma = 0
    notas = 0
    opcao = 0

    while notas < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            notas += 1
            soma += nota
        else:
            print("nota invalida")
        
    media = soma / 2

    print(f"media = {media:.2f}")

    while 1 > opcao or opcao > 2:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())

        if opcao == 1:
            calcula_media()
        elif opcao == 2:
            return

calcula_media()