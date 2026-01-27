# Переборное решение задания 22
for i in range(1,10000):
    x = i
    x0 = x
    N = 0
    while x > 0:
        d = x % 3
        N = 10 * N + d
        x = x // 3
    N += x0
    if N >= 100000:
        print(i)