from fnmatch import *

ans = []
for i in range(0, 10**5):
    s = str(i)
    s = "20" + s + "23"
    r = int(s)

    if fnmatch(s, "20*23"):
        ans.append(r)

ans.sort()

print("2023", ans)