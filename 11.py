'''11. Дані про температуру води на Чорноморському узбережжі за декаду
вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
купання.'''
import numpy as np
import random as rd
aa = [rd.randint(2,30) for i in range(10)]
bb = np.array(a)                                   #Створення масиву
print('Температура води з 1 по 10 вересня:')
print(b)
kk = 0 
for j in a:                                        #Проходим по елементах масиву 
    if 22 < j < 24:                                #Перевіряємо умову 
        k += 1
print(f'Дні придатних для купання: {k}')
