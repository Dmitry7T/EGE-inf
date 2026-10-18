f = [int(x) for x in open("17.txt")]

ans = []

for i in range(len(f) - 2):
    if 99 < f[i + 1] < 1000 and f[i + 1] % 10 == 5:
        ans.append(f[i] + f[i + 1] + f[i + 2])

print(len(ans), max(ans))