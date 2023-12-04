# Caio Cesar 02/12/23
# BEE 1131

def grenais(time1, time2, empate):
    inter = time1
    gremio = time2
    empates = empate
    opcao = 0

    placar = input().split()
    if placar[0] > placar[1]:
        inter += 1
    elif placar[1] > placar[0]:
        gremio += 1
    else:
        empates += 1

    while 1 > opcao or opcao > 2:
        print("Novo grenal (1-sim 2-nao)")
        opcao = int(input())

        if opcao == 1:
            grenais(inter, gremio, empates)
        elif opcao == 2:
            print(f"{inter + gremio} grenais")
            print(f"Inter:{inter}")
            print(f"Gremio:{gremio}")
            print(f"Empates:{empates}")

            if inter > gremio:
                print("Inter venceu mais")
            elif gremio > inter:
                print("Gremio venceu mais")
            else:
                print("Nao houve vencedor")

            return

grenais(0, 0, 0)