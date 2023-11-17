# Caio Cesar 13/11/23
# BEE 1052

meses = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

entrada = int(input())

for k in meses.keys():
    if k == entrada:
        print(meses[k])
        break
