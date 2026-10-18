from itertools import *

tab = "346 45 16 125 247 137 56".split()
pic = "EG GD DF FA AB BC CE ED CA".split()

print(*range(1, 8))
for var in permutations("ABCDEFG"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(*var) # 14