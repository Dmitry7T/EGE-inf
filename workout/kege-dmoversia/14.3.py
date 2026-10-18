import numpy as np
s = 7 ** 100 * (7 ** 70 + 1)

for x in range(2030, 0, -1):
    z = np.base_repr(s - x, base=7)
    if (z.count('0') == 71):
        print(x)
        break