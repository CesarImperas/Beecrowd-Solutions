# Caio Cesar 11/11/23
# BEE 1837

entrada = input().split()
num_a = int(entrada[0])
num_b = int(entrada[1])

num_r = 0
while num_r < abs(num_b):
    if (num_a - num_r) % num_b == 0:
        num_q = (num_a - num_r) // num_b
        break
    num_r += 1

print(f'{num_q} {num_r}') # type: ignore