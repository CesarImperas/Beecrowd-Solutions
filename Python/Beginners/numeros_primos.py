# Caio Cesar 25/10/23
# BEE 2159

from math import log

num = int(input())

var_P = (num/log(num))
var_M = 1.25506 * (num/log(num))

print(f'{var_P:.1f} {var_M:.1f}')