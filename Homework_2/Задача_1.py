# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

str_num = str(input('Введите вещественное число: '))
print(str_num)
sum = 0

for i in str_num:
    if i.isdigit():
        sum +=int(i)

print(f'Сумма цифр = {sum}')


