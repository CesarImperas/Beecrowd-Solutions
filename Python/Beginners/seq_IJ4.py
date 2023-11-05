# Caio Cesar 03/11/23
# BEE 1098

num_i = 0
num_j = 1
for i in range(10):
    if num_i == 0 or num_i == 1:
        print(f'I={num_i:.0f} J={num_j:.0f}')
        print(f'I={num_i:.0f} J={num_j + 1:.0f}')
        print(f'I={num_i:.0f} J={num_j + 2:.0f}')

    else:
        print(f'I={num_i:.1f} J={num_j:.1f}')
        print(f'I={num_i:.1f} J={num_j + 1:.1f}')
        print(f'I={num_i:.1f} J={num_j + 2:.1f}')

    num_i += 0.2
    num_j += 0.2

print(f'I=2 J=3')
print(f'I=2 J=4')
print(f'I=2 J=5')