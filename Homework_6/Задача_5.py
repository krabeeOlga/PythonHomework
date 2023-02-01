# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

from random import randint as RI 

num = int(RI(3,8))
my_list1 = [(RI(0,100)) for i in range (num)]
print(*my_list1,  sep=', ')

my_list2 = my_list1

for i in range(num):
    index = RI(0, len(my_list2)-1)
    temp = my_list2[i]
    my_list2[i] = my_list2[index]
    my_list2[index] = temp

print(*my_list2, sep=', ')