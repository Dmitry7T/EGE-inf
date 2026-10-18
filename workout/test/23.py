from collections import defaultdict
from functools import cache

graph = defaultdict(dict)
for line in open("demo_23__bgfr4.txt"):
    u, v, w = line.split()
    graph[u][v] = int(float(w))


@cache
def find(node):
    if node == "100":
        return 0

    res = float("inf")
    for neighbor, weight in graph[node].items():
        res = min(res, weight + find(neighbor))
    return res


print(find("1"))