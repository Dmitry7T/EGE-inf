from itertools import *

i = 0
for k in range(3, 8):
    for s in product("СЕПИЯ", repeat=k):
        if s.count('Е') <= 2 and s.count('И') <= 2 and s.count('Я') <= 2 and all(x not in "СП" for x in s[1:]):
            i += 1

print(i)