P = range(35, 56)
Q = range(45, 66)

ans = []

def f(x, A):
    return ((x in P) <= (x in A)) and ((x not in A) <= (x not in Q))

for a in range(0, 200):
    for b in range(a, 200):
        A = range(a, b)

        if all(f(x, A) for x in range(1000)):
            ans.append(len(A))

print(min(ans) - 1) # 30