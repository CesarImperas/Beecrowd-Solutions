# Caio Cesar 01/12/23
# BEE 1049

cadeia = {"vertebrado": {"ave": {"carnivoro": "aguia", "onivoro": "pomba"}, "mamifero": {"onivoro": "homem", "herbivoro": "vaca"}},
        "invertebrado": {"inseto": {"hematofago": "pulga", "herbivoro": "lagarta"}, "anelideo": {"hematofago": "sanguessuga", "onivoro": "minhoca"}}}

coluna = input()
classe = input()
alimento = input()

animal = cadeia[coluna][classe][alimento]

print(animal)