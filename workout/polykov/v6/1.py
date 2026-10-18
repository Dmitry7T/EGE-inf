from itertools import *

tab  = "2346 16 1678 17 68 1235 34 35".split()
pic = "AB BD DG GE EH HF FC CA BE EC CB".split()

print(*range(1, 9))

for var in permutations("ABCDEFGH"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(*var) # 78