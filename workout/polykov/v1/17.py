arr = [int(x) for x in open("17.txt")]

ans = []
for i in range(len(arr) - 3):
    a1, a2, a3, a4 = abs(arr[i]), abs(arr[i + 1]), abs(arr[i + 2]), abs(arr[i + 3])
    if a1 % 2 != a2 % 2 and a2 % 2 != a3 % 2 and a3 % 2 != a4 % 2:
        ans.append(arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3])

print(len(ans), max(ans))