def m(a, b):
    return [(a + 4, b), (a * 2, b), (a, b + 4), (a, b * 2)]

def w(a, b):
    return any(x + y >= 133 for x, y in m(a, b))

results = []
for S in range(1, 116):
    if w(17, S):
        continue

    for a, b in m(17, S):
        if w(a, b):
            continue
        if all(w(c, d) for c, d in m(a, b)):
            results.append(S)
            break


print(*results)