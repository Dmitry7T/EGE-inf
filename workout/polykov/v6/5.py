res = []

for N in range(10000, 10**5):
    s = oct(N)[2:]
    s = "".join([x if x not in "1357" else '2' for x in s])
    s += str(N % 8)
    R = int(s, 8)

    s = oct(R)[2:]
    s = "".join([x if x not in "1357" else '2' for x in s])
    s += str(N % 8)
    R = int(s, 8)

    if R % 2023 == 0:
        res.append(N)


print(sum(res)) # 197535