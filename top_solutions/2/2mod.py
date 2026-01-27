# Упрощенный вариант решения для задачи с использованием модуля itertools
# В функцию task2 вводим данную нам в задаче формулу
from itertools import product

def task2(x, y, z, w):
    return not(y <= (x == w)) and (z == x)

print('x y z w')

for (x, y, z, w) in product([0, 1], repeat=4):
    if task2(x, y, z, w): print(x, y, z, w)