x = 7 ** 1003 * (1 + 6*7) - 3 * 7 ** 57 + 294

import numpy as np

x = np.base_repr(x, base=7)

count = 0
for i in x:
    count += int(i)

print(count)