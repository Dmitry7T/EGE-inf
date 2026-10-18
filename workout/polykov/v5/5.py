ans = []
for N in range(0, 10000000):
    s = str(N)
    S1 = [int(x) for x in s if int(x) % 2 == 0]
    S1 = sum(S1) if len(S1) != 0 else 0

    S2  = N % 10 + N // 100 % 10 + N // 10000 % 10 + N // 1000000 % 10 + N // 100000000 % 10

    R = abs(S1 - S2)

    #print(N, S1, S2, R)

    if R == 26:
        ans.append(N)

print(min(ans)) # 1070909