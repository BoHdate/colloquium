"""
14. Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.

Олійник Богдан Сергійович 122\Д
"""
import numpy as np
a = []
b = int(input('Введіть висоту:'))
c = 0
for i in range(1,10):
    c = b - ((10 * i ** 2) / 2)
    if c < 1: break
    a.append(c)
j = np.array(a)
print(f'Масив пройдених відстаней:\n {j}')
