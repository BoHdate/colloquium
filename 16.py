"""
16. Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.

Олійник Богдан Сергійович 122\Д
"""
import numpy as np
import random as rd 
a = np.array([rd.randint(10,500) for i in range(20)])
b = []
c = 0 
print(a)
for g in a:                             #Проходимо по елементах 
    if g % 7 == 0:                             
     b.append(g)                        #Додаємо до списку 
     c += 1
if c == 0:
      print('Елементів кратних 7-ми не виявлено')
      exit(0)
k = np.array(b)
print(f'Елементи кратні 7-ми: {k}')
print(f'Добуток: {k.prod()}')