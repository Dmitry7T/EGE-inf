from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n <= 5: return n + 15

    if n > 5 and n % 2 == 0: return f(n // 2) + n ** 3 - 1
    if n > 5 and n % 2 == 1: return f(n - 1) + 2 * n ** 2 + 1

i = 0
for n in range(1, 1001):
    if str(f(n)).count('8') >= 2:
        i += 1

print(i)