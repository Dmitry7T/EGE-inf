def f(x, p):
    if x >= 51 or p > 2: return p == 2

    if x % 2 == 0:
        return 0

    return f(x * 3, p + 1) or f(x + 1, p + 1) or f(x + 3, p + 1)


res = [S for S in range(1, 51) if f(S, 0)]
print(*res) # 7