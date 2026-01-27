# Задание 8(на перестановки букв)
from itertools import permutations
cnt = 0
for i in permutations("ВИКАЯ", r=4):
    if "ИЯ" not in "".join(i):
        cnt += 1
print(cnt)