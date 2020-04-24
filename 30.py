"""
30. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.

Олійник Богдан Сергійович 122\Д
"""
import numpy as np
import random as rd 
a = [rd.randint(1,10) for i in range(10)]
b = np.array(a)
print(b)
print(f'Індекс мінімального елементу:{a.index(b.min())}')
c = np.array(a[a.index(b.min()):])
print(f'Зріз:{c}')
print(f'Середнє значення елементів зрізу:{c.mean()}')
