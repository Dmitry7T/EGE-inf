from itertools import *

def f(x, y, z, w):
    return ((z <= w) <= (not y)) and x

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(0, 0, 1, a1), (a2, a3, 0, a4), (0, a5, 1, 1)]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 0]:
                print(*p, sep='') # zywx