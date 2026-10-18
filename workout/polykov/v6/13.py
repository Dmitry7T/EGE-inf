# 112.160.0.0
# 255.240.0.0

# 01110000.10100000.0.0
# 11111111.1111 0000.00000000.00000000

from itertools import *

c = 0
for x in product("01", repeat = 8 + 8 + 4):
    s = x.count('1') + 5

    if s % 5 == 0:
        c += 1

print(c)

print(bin(112))
print(bin(160))
print(bin(240))