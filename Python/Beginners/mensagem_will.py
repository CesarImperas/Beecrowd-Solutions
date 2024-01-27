# Caio Cesar 27/1/24
# BEE 2523

while True:
    try:

        string = input()

        length = int(input())

        pos = [int(n) for n in input().split()]

        word = ""

        for i in range(length):
            char = string[pos[i]-1]
            word += char

        print(word)
        
    except EOFError: break