from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n == 0:
        return 0

    if n % 2:
        return 3 + f(n - 1)
    else:
        return f(n/2) - 1


ans = set()

for n in range(1000):
    ans.add(f(n))

print(len(ans))