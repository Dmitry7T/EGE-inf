# Задание 19-21 на одну кучу
def WIN1(s):
    return (s + 1 >= 29) or (s * 2 >= 29)
def LOSS1(s):
    return (not WIN1(s)) and WIN1(s + 1) and WIN1(s * 2)
def WIN2(s):
    return LOSS1(s+1) or LOSS1(s*2)
def LOSS12(s):
    return (WIN1(s + 1) and WIN2(s * 2)) or (WIN2(s + 1) and WIN1(s * 2))

s19, s20, s21 = [], [], []
for s in range(1,29):
    if LOSS1(s):
        s19.append(s)
    if WIN2(s):
        s20.append(s)
    if LOSS12:
        s21.append(s)
print(s19,s20, s21)