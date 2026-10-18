times = [int(x) for x in open("26.txt")]
times.pop(0)
times.sort()

boilers = {}
for t in times:
    flag = False
    for boiler in boilers.keys():
        if boilers[boiler] <= t:
            boilers[boiler] = t + 6
            flag = True
            break
    if not flag:
        boilers[len(boilers)] = t + 6

min_bolers_count = len(boilers)
print(min_bolers_count) # 38