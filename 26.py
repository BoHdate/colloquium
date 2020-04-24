"""
26. Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри температури виробляються
шість раз на добу і результати вводяться з клавіатури у масив T.

Олійник Богдан Сергійович 122\Д
"""
import numpy as np
b = []
for i in range(1,7):
    x = int(input(f'Замір {i} = '))
    b.append(x)                                  #Додаємо до списку 
T = np.array(b)
print(f'Заміри температури:{T}')                    
print(f'Максимальна: {T.max()}')                    #Виводимо Max значення 
print(f'Мінімальна: {T.min()}')                     #Виводимо Min значення 
print(f'Середня: {T.mean()}')                       #Виводимо середнє значення 