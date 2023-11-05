# Caio Cesar 03/11/23
# BEE 1095

num_i = 0
for i in range(60, -5, -5):
    num_j = i
    if num_j == 60:
        num_i += 1
    else:
        num_i += 3
    print(f'I={num_i} J={num_j}')