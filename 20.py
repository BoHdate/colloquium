"""
20. Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.

Олійник Богдан Сергійович 122\Д 
"""

import numpy as np
import random as rd 
n = int(input('n = '))
a = [rd.randint(50,100) for i in range(20)]
b = np.array(a)
print(b)
c = []
k = 0
for g in b:                                     #Проходимо по елементах 
    if g > n:
     c.append(g)                                #Додаємо елементи що проходять умову до списка 
    k += 1
if k == 0:
    print('Елементів що задовільняють умову не виявлено')
    exit(0)
j = np.array(c)
print('Елементи більші за n:',j)
print(f'Сума:{j.sum()}')
