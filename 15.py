"""
15. Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -20.
Заповнення масиву здійснити випадковими числами від 100 до 200.


"""

import numpy as np
import random as rd 
a = np.array([rd.randint(100,200) for i in range(20)])
b = []
c = 0 
print(a)
for i in a:                                             #Проходим по елементах масиву 
    if i % 2 == 0:
     b.append(i)                                        #Додаємо елементи що проходять умову до списка 
     c += 1
if c == 0:
    print('Парних елементів не було виявлено')
    exit()                                              
k = np.array(b)
print(f'Парні числа:{k}')
print(f'Сума:{k.sum()}')