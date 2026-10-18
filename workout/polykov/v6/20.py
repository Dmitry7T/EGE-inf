def f(x, p):
    if x >= 51 or p > 3: return p == 3

    if x % 2 == 0 and p != 0:
        return 0

    return f(x * 3, p + 1) or f(x + 1, p + 1) or f(x + 3, p + 1)


res = [S for S in range(1, 51) if f(S, 0)]
print(*res) # 12 14