P = range(80, 104)
Q = range(5, 16)
R = range(35, 51)

ans = []
for a in range(0, 110):
    for b in range(a, 110):
        A = range(a, b)
        if all(((x in P) <= (x in Q)) or (not(x in A) <= (x in R)) for x in range(1000)):
            ans.append(len(A))


print(min(ans) - 1)