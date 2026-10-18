f = [int(x) for x in open("17.txt")]

ans = []
minel = float("inf")
for i in f:
    if 9 < i < 100 and not i % (i % 10 + i // 10 % 10):
        if i < minel: minel = i

for i in range(len(f) - 1):
    if not f[i] % minel or not f[i + 1] % minel:
        ans.append(f[i] + f[i + 1])

print(len(ans), max(ans))