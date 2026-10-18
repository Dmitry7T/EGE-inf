def f(n):
    if n <= 5: return n
    elif n % 4 == 0: return n + f(n / 2 - 1)
    elif n % 4: return n + f(n + 2)

res = []
for i in range(100):
    try:
        x = f(i)
        res.append(i)
    except RecursionError:
        continue

print(max(res)) # 12