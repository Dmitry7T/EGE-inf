f = [int(x) for x in open("18.txt")]

res = []

for num in range(len(f) - 11):
    for i in range(num + 11, len(f)):
        a1, a2 = f[num], f[i]

        if a1 + a2 < 200:
            res.append(a1 + a2)


print(len(res)) # 8558