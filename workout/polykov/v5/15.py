B = range(160, 181)

def f(x, A):
    return (x in B) <= ((x % 35 == 0) <= (x % A == 0))

ans = []
for A in range(1, 10000):
    if all(f(x, A) for x in range(10000)):
        ans.append(A)

print(len(ans)) # 6