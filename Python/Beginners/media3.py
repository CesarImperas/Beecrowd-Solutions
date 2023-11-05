# Caio Cesar 14/9/23
# BEE 1040

entrada = input().split()

n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])
n4 = float(entrada[3])

media_pon = ((n1*2)+(n2*3)+(n3*4)+(n4*1)) / 10

print(f'Media: {media_pon:.1f}')

if media_pon >= 7.0:
    print('Aluno aprovado.')
elif media_pon < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n5 = float(input())
    print(f'Nota do exame: {n5}')
    media_nova = (n5+media_pon) / 2
    if media_nova >= 5.0:
        print(f'Aluno aprovado.')
        print(f'Media final: {media_nova:.1f}')
    else:
        print(f'Aluno reprovado.')
        print(f'Media final: {media_nova:.1f}')