import sys

sys.setrecursionlimit(10000)

def f(n):
    if n == 1: return 1

    if n > 1:
        return n * f(n - 1)

print((f(3038) + 5*f(3037)) / f(3036))
