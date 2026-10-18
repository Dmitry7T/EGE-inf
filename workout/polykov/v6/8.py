from itertools import *

res = []
for x in product("ОБЩЕСТВ", repeat = 5):
    s = "".join(x)
    if s[0] not in "БЩ" and s[-1] == s[-2] == 'В' and not "ВЕ" in s and not "ЕВ" in s and "ТБ" in s:
        res.append(x)

print(len(res)) # 11