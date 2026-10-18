from itertools import *

tab = "256 13 245 356 134 14".split()
pic = "CB  BE EA AF FC FD DB DE".split()

print(*range(1, 7))
for var in permutations("ABCDEF"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(*var)