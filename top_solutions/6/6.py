# перевод из 10сс в любую другую до 36cc с помощью модуля numpy
for i in range(1, 10000):
    s = i
    n = 0
    while s <= 375:
        s = s + 5
        n = n + 2
    if n < 295:
        print(i)