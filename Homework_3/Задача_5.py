# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def input_number():
    while True:
        try:
            num = int(input('Введите целое положительное число: '))
            if num > 0:
                return num
            else:
                print('Нужно положительное число!')
        except:
            print('Вы ввели что-то не то!')

num = input_number()

my_list1 = []
my_list1.extend([0, 1])

for i in range (2, num + 1):
    my_list1.append(my_list1[i - 1] + my_list1[i - 2])

# print(my_list1)

my_list2 = []
my_list2.extend([1, -1])

for i in range (2, num):
    my_list2.append(my_list2[i - 2] - my_list2[i - 1])

my_list2.reverse()

# print(my_list2)

my_list3 = []

for i in my_list2:
    my_list3.append(i)
for i in my_list1:
    my_list3.append(i)

print(my_list3)

