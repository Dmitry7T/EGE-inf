def d(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

stars = [list(map(float, i.split())) for i in open("B.txt")]

eps = 1

clusters = []
while len(stars) > 0:
    cluster = [stars[0]]
    stars.pop(0)
    i = 0
    while i < len(cluster):
        j = 0
        while j < len(stars):
            if d(cluster[i][0], cluster[i][1], stars[j][0], stars[j][1]) < eps:
                cluster.append(stars[j])
                stars.pop(j)
            j += 1
        i += 1
    clusters.append(cluster)

print("clusters: ", len(clusters))

centroids = []
for cluster in clusters:
    centroid = []
    min_d = float("inf")
    for star in cluster:
        star_d = 0
        for substar in cluster:
            star_d += d(star[0], star[1], substar[0], substar[1])
        if star_d < min_d:
            min_d = star_d
            centroid = star
    centroids.append(centroid)

Px = abs(int(sum([centroid[0] for centroid in centroids]) / len(centroids) * 10000))
Py = abs(int(sum([centroid[1] for centroid in centroids]) / len(centroids) * 10000))

print(Px, Py)