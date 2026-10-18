from itertools import *

res = set()
for c in product("52", repeat=7):
    num = 216
    for i in c:
        if i == '5':
            num -= 5
        if i == '2':
            num *= -2
    if num >= 0:
        res.add(num)

print(len(res)) # 39