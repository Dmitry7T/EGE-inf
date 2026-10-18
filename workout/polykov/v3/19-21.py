def f(x, p):
    if x <= 40 or p > 4: return p == 2 or p == 4

    if p % 2:
        return f(x - 2, p + 1) or f(x - 4, p + 1) or f(x // 3, p + 1)
    else:
        return f(x - 2, p + 1) and f(x - 4, p + 1) and f(x // 3, p + 1)
    
ans =[S for S in range(41, 1000) if f(S, 0)]
print(ans)