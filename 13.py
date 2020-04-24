"""
13. Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.

Олійник Богдан Сергійович 122\Д 
"""

import numpy as np
import random as rd
a = [rd.randint(-6,5) for i in range(15)]
b = np.array(a)
print(b)
print(f'Min значення: {a.min()}')
