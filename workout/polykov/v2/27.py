eps = 0.5

from math import *

def d(x1, y1, x2, y2): return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

stars = [list(map(float, x.split())) for x in open("27_A.txt")]
clusters = []
while len(stars):
    cluster = []
    cluster.append(stars[0])

    i = 0
    while i < len(cluster):
        j = 0
        while j < len(stars):
            if d(*cluster[i], *stars[j]) <= eps:
                cluster.append(stars[j])
                stars.pop(j)
            else:
                j += 1
        i += 1
    clusters.append(cluster)

print("колличество кластеров (с аномалиями): ", len(clusters))

for cluster in clusters:
    if len(cluster) < 10: 
        clusters.remove(cluster)
        print("аномалии удалены")

centroids = []
for cluster in clusters:
    sums = []
    for star in cluster:
        sum = 0
        for sub_star in cluster:
            sum += d(*star, *sub_star)
        sums.append(sum)
    centroids.append(cluster[sums.index(min(sums))])

print(centroids)

Px = 0
Py = 0
for centroid in centroids:
    Px += centroid[0]
    Py += centroid[1]

Px /= len(centroids); Px *= 10000
Py /= len(centroids); Py *= 10000

print(Px, Py)