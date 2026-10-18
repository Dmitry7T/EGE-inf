from itertools import *

tab = "26 15 67 6 26 13457 36".split()
pic = "АБ БВ ВГ ГА ГД ГЖ ЖЕ ЕГ".split()

print(*range(1, 8))

for var in permutations("АБВГДЕЖ"):
    if all(str(var.index(x) + 1) in tab[var.index(y)]for x, y in pic):
        print(*var)