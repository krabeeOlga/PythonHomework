# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint as RI 
my_list = []

for i in range (int(RI(4,8))):
    my_list.append(RI(1,10))

print(my_list)

result = []

for i in range (len(my_list)):
    result.append(my_list[i]*my_list[len(my_list)-i-1])

for i in range (len(result)):
    if i > (len(result)/2):         
        del result[-1]        

if len(my_list) % 2 == 0:
    del result[-1]

print(result)
    

   



