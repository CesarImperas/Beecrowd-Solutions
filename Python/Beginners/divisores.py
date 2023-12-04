# Caio Cesar 02/12/23
# BEE 1157

num = int(input())

for n in range(1, num + 1):
    if n % num == 0 or num % n == 0:
        print(n)