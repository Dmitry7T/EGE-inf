f = [int(x) for x in open("17.txt")]

min_el = float("inf")
for it in f:
    if it % 103 == 0:
        min_el = min(min_el, it)


res = []
for i in range(len(f) - 1):
    a1, a2 = f[i], f[i + 1]

    if (a1 + a2) % 2 == 0 and abs(a1 - a2) % min_el == 0:
        res.append(a1 + a2)

print(len(res), max(res)) # 4 145300