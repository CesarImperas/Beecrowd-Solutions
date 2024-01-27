# Caio Cesar 27/1/24
# BEE 1253

testes = int(input())

for _ in range(testes):
    string = input()
    number = int(input())

    new = ""

    for char in string:
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        pos = alphabet.index(char)
        new_pos = pos - number

        new += alphabet[new_pos]

    print(new)
