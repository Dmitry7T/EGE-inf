from itertools import *

tab = "247 148 578 126 38 47 136 235".split()
pic = "AB BH HF FD DC CE EA AH EG GF GC".split()

print(*range(1, 9))

for var in permutations("ABCDEFGH"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(*var) # 30+8 = 38