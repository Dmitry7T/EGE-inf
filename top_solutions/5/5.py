# Программа решения конкретного 5-го задания, реализован вариант с дублированием цифры и добавлением остатка от деления суммы цифр на 2

# перевод из 10сс в любую другую до 36cc с помощью модуля numpy
#import numpy as np
#x = np.base_repr(10, base=3) # x = str()

def R(N):
    b_bin = bin(N)[2:]
    n_bin = n_bin + n_bin[-1]
    n_bin += str(n_bin.count('1') % 2)
    return int(n_bin, 2)

for n in range(1, 1000):
    if R(n) > 97:
        print(R(n))
        break 