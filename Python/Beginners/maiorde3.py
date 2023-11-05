# Caio Cesar
# BEE 1013

num = input().split()

num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])

maior1e2 = int((num1+num2+abs(num1-num2))/2)

if maior1e2 > num3:
    print(f'{maior1e2} eh o maior')
else:
    print(f'{num3} eh o maior')