# Петя 1 

def f1(x, p):
    if x >= 311 or p > 2: return p == 2

    if p % 2 == 1:
        return f1(x + 3, p + 1) or f1(x + 5, p + 1) or f1(x * 2, p + 1)
    else:
        return f1(x + 3, p + 1) and f1(x + 5, p + 1) and f1(x * 2, p + 1)


res1 = [S for S in range(311) if f1(S, 0)]
print(sum(res1)) # 462

print()
def f2(x, p):
    if x >= 311 or p > 3: return p == 3

    if p % 2 == 1:
        return f2(x + 3, p + 1) and f2(x + 5, p + 1) and f2(x * 2, p + 1)
    else:
        return f2(x + 3, p + 1) or f2(x + 5, p + 1) or f2(x * 2, p + 1)


res2 = [S for S in range(311) if f2(S, 0)]
print(res1)
print(res2) # 77 152

print()
def f3(x, p):
    if x >= 311 or p > 4: return p == 4

    if p % 2 == 1:
        return f3(x + 3, p + 1) or f3(x + 5, p + 1) or f3(x * 2, p + 1)
    else:
        return f3(x + 3, p + 1) and f3(x + 5, p + 1) and f3(x * 2, p + 1)


res3 = [S for S in range(311) if f3(S, 0)]
print(res1)
print(res2)
print(res3)