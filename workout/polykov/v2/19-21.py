def f(x, p):
    if p > 4 or x >= 51:
        return p == 4

    if p > 0 and x % 2 == 0:
        return 0

    return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x * 3, p + 1)

ans = [s for s in range(1, 51) if f(s, 0)]
print(ans)