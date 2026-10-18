from itertools import *

tab = "2345 135 12467 1356 124 347 36".split()
pic = "АБ БЕ ЕЖ ЖД ДВ ВА АГ ГБ БД ДГ ГВ ДЕ".split()

print(*range(1, 8))

for var in permutations("АБВГДЕЖ"):
    if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
        print(*var) # ГВДБАЕЖ