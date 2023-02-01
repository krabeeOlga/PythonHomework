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

my_list1 = [0, 1]
[my_list1.append(my_list1[-2]+my_list1[-1]) for i in range(num - 1)]

my_list2 = [1, -1]
[my_list2.append(my_list2[i] - my_list2[i+1]) for i in range(num-2)]
my_list2.reverse()

print(my_list2 + my_list1)
