def f(x, p):
    if x == 0 or p > 1:
        return p == 1

    if x >= 5:
        if p % 2 == 0:
            return f(x - 5, p + 1) or f(x // 3, p + 1)
        else:
            return f(x - 5, p + 1) and f(x // 3, p + 1)

    else: 
        return f(x // 3, p + 1)

print([s for s in range(1, 100) if f(s, 0)])