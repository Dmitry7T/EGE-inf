from itertools import *

tab = "24 146 56 1267 36 23457 46".split()
pic = "АБ БВ ВД ДЕ ЕК КГ ГЕ ЕВ ВА ВГ".split()

print(*range(1, 8))
for var in permutations("АБВГДЕК"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(*var) # 40