from itertools import *

def A(x):
    return x + 1

def B(x):
    if (x // 10) % 10 < x % 10:
        return 100 + x % 10 * 10 + (x // 10) % 10


