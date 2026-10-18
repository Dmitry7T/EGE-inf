ans =[]

for N in range(1000):
    s = bin(N)[2:]

    if N % 3:
        s += bin(N % 3 * 3)[2:]

    else:
        s += s[len(s)-3:]
        #print(s if N == 12 else '')

    R = int(s, 2)

    if R >= 200:
        ans.append(N)

print(min(ans)) # 26