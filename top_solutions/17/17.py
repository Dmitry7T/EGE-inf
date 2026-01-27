# По сути меняется лишь 7 строчка с условием
f = open("task17.txt")
a = []
sum_pari = []
for s in f:
    a.append(int(s))
for i in range(len(a)-1):
    if a[i]*a[i+1] % 3 == 0:
        sum_pari.append(a[i]+ a[i+1])
print(len(sum_pari),max(sum_pari))