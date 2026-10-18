ans = []
for N in range(10000):
    s = bin(N)[2:]

    if s.count('1') > s.count('0'):
        s += '0'
    else:
        s = "11" + s

    if s.count('1') > s.count('0'):
        s += '0'
    else:
        s = "11" + s

    R = int(s, 2)
    if R > 500:
        ans.append(N)

print(min(ans)) # 32