# Caio Cesar 27/1/24
# BEE 3147

exercito = [int(n) for n in input().split()]

bem = exercito[0] + exercito[1] + exercito[2] + exercito[5]
mal = exercito[3] + exercito[4]

if bem >= mal:
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.") 