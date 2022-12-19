# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


num = int(input('Введите число: '))
my_list = []

for i in range(num):
    my_list.append(round(((1 + 1/(i+1))**(i+1)),2))
    if (my_list[i] % 1) == 0:
        my_list[i] = round(my_list[i])

print(f'Для n={num} -> {my_list}')

sum = 0
for i in range(num):
    sum += my_list[i]

print(round(sum,2))


