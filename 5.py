"""
5. Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.

Олійник Богдан Сергійович 122\Д
"""
import numpy as np
import random as rd
a = np.array([rd.randint(2,5) for i in range(7)])    #Створюємо масив 
print(a)
a_new = a.copy()
for g in range(len(a_new)):                          #Проходим по елементах масиву
    a_new[g]*= 2                                     #Збільшуємо в 2 раза елементи 
print(a_new)
