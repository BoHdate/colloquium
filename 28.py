"""
28. Знайти кількість парних елементів одновимірного масиву.

Олійник Богдан Сергійович 122\Д
"""
import numpy as np
import random as rd 
b = []
a = np.array([rd.randint(1,10) for i in range(10)])
print(a)
k = 0
for g in a:                                                 #Проходимо по елементах
    if g % 2 == 0:
        b.append(g)                                         #Додаємо до списку 
        k += 1
if k == 0:
    print('Парних елементів не було виявлено')
    exit(0)
j = np.array(b)
print(f'Парні елементи:{j}')
print(f'Кількість:{j}')
