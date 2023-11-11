# Caio Cesar 06/11/23
# BEE 1847

def humor(temp):
    dia1 = int(temp[0])
    dia2 = int(temp[1])
    dia3 = int(temp[2])

    if dia1 > dia2:
        if dia3 > dia2: return True
        else:
            if (dia2 - dia3) < (dia1 - dia2): return True
            else: return False

    elif dia2 > dia1:
        if dia2 > dia3: return False
        else:
            if (dia2 - dia3) > (dia1 - dia2): return False
            else: return True
            
    else:
        if dia3 > dia1: return True
        else: return False

temperaturas = input().split()

if humor(temperaturas):
    print(':)')
else:
    print(':(')