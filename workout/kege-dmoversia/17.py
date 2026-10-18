f = open("C:\\Users\\User\\Desktop\\All\\Programming\\EGE-inf\\workout\\kege-dmoversia\\17.txt")
arr = f.read().split("\n")
arr = [int(x) for x in arr]

min_el = min(arr)
ans = []

for i in range(len(arr) - 1):
    if arr[i] % 33 == min_el or arr[i + 1] % 33 == min_el:
        ans.append(arr[i] + arr[i + 1])

print(len(ans), max(ans))