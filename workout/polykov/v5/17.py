f = [int(x) for x in open("17.txt")]

min_el = float("inf")
for x in f:
    if x % 21 == 0:
        min_el = min(min_el, x)

res = []
for i in range(len(f) - 1):
    a1 = f[i]
    a2 = f[i + 1]

    diff = abs(a1 + a2 - 2 * min_el)
    if diff % 2 == 0:
        half_diff = diff // 2
        root = int(half_diff ** 0.5)
        if root * root == half_diff:
            res.append(a1 * a2)

print(len(res), min(res)) # 40 41441