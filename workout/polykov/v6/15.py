def f(x, y, A):
    return (5*x - 6*y < A) or (x - y > 30)

for A in range(1000):
    if all(f(x, y, A) for x in range(1000) for y in range(1000)):
        print(A) # 151
        break