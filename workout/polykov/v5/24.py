f = open("24.txt").read()

cur = f[0]      
max_res = f[0]  

for i in range(1, len(f)):
    if f[i] > f[i-1]:
        cur += f[i]
    else:
        if len(cur) > len(max_res):
            max_res = cur
        cur = f[i]

if len(cur) > len(max_res):
    max_res = cur
    
print(max_res) # 3BEHUkvy