"""
19. Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300.

Олійник Богдан Сергійович 122\Д
"""

import numpy as np
import random as rd
a = []
b = [rd.randint(200,300) for i in range(20)]
k = 0
print(b)
for g in b:                                     #Проходимо по елементах 
    if g % 2 == 3:
        b.append(g)                             #Додаємо елементи що проходять умову до списка 
        k += 1
if k == 0:
    print('Елементів що задовільняють умову не виявлено')
    exit(0)
j = np.array(b)
print(f'Елементи, що задовільняють умову:{j}')
print(f'Сума:{j.sum()}')