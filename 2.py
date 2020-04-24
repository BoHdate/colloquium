"""
2. Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву

Олійник Богдан Сергійович 122\Д
"""
import numpy as np
import math
a = list()
for i in range(1,6):                    #Виводимо числа 
    x = (int(input(f'Число {i} = ')))
    a.append(x)                         #Додаємо числа до списку 
b = a[:]
j = np.array(a)                         #Створюємо масив зі списку 
for elm in a:
    print(elm ** elm)
for c in b:
    print(math.sqrt (c))
