# Задание 8(на системы счисления)
from itertools import product
cnt = 0
for i in product("DLORW", repeat=5):
    cnt += 1
    if i[0] == "L":
        print(cnt)