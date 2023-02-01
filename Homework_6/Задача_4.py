# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI 
from functools import reduce

my_list = [(RI(0,10)) for i in range (int(RI(4,8)))]
print(my_list)

filtered = [y for x,y in enumerate(my_list) if x % 2 != 0]
sum = reduce(lambda x, y:x+y, filtered)

print(f'Сумма элементов на нечетных позициях = {sum}')
