def f(n, m):
    return n % m == 0

B = range(70, 91)
for A in range(1000, 0, -1):
    if all(f(x, A) or ((x in B) <= (not(f(x, 22)))) for x in range(1000)):
        print(A)
        break