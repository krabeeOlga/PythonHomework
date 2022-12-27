# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
my_list = []

for i in range (5):
    my_list.append(round(random.uniform(0,10), 2))  
    
print(my_list)

result = []

for i in range (5):
    result.append(int(my_list[i]*100)%100)
    
print((max(result) - min(result))/100)
