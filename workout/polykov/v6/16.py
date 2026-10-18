import sys
sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(100000)

def f(n):
    if n >= 5000:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
    else:
        return (2 * f(n + 1)) // (n + 1)

print(1000 * f(7) // f(4)) # 26250
