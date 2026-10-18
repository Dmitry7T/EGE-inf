ans = []

for N in range(1000):
    s = bin(N)[2:]

    s += s[-1]

    if s.count('1') % 2:
        s += '0'
    else:
        s += '1'

    if s.count('1') % 2:
        s += '0'
    else:
        s += '1'

    r = int(s, 2)

    if r > 130:
        ans.append(N)

print(min(ans))