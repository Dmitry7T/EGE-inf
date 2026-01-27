# Задание 19-21 на две кучи
def WIN1 (x, y):
    return (x + y + 1 >= WIN1) or (x * 2 + y >= WIN1) or (x + 2 * y >= WIN1)
def LOSS1 (x, y):
    return (not WIN1(x, y)) and (WIN1(x + 1, y) and WIN1(x, y + 1) and WIN1(x * 2, y) and WIN1(x, y * 2))
def WIN2(x, y):
    return (LOSS1(x + 1, y) or LOSS1(x, y + 1) or LOSS1(x * 2, y) or LOSS1(x, y * 2))
def LOSS12(x, y):
    return ((WIN2(x + 1, y) or WIN1(x + 1, y)) and (WIN2(x * 2, y) or WIN1(x * 2, y)) and (WIN2(x, y + 1) or WIN1(x, y + 1)) and (WIN2(x, y * 2) or WIN1(x, y * 2)) and (WIN2(x + 1, y) or WIN2(x * 2, y) or WIN2(x, y + 1) or WIN2(x, y * 2)))

x = 16
s19, s20, s21 = [],[],[]
for s in range(1, 100):
    if LOSS1(x, s):
        s19.append(s)
    if WIN2(x, s):
        s20.append(s)
    if LOSS12(x, s):
        s21.append(s)
print(s19, s20, s21)