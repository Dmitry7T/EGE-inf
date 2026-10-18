from itertools import *

i = 1
for var in permutations("БДНОРЫЯ"):
    if i == 3377:
        print(*var)
        break

    i += 1