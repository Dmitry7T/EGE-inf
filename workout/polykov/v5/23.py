f = open("23.txt")

edges = []
for line in f:
    l, m, w = line.split()
    if int(m) == 633:
        continue
    edges.append([int(l), int(m), float(w)])

min_dist = [float("inf")] * 1001
min_dist[1] = 0

for i in edges:
    for j in edges:
        start, end, weight = j
        min_dist[end] = min(min_dist[end], min_dist[start] + weight)

print(int(min_dist[100])) # 11782