# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def input_num():
    while True:
        try:
            num = int(input('Введите целое десятичное число: '))
            return num
        except:
            print('Вы ввели что-то не то!')

num = input_num()

my_str = ''

while num > 0:
    my_str += str(num % 2)
    num = num // 2

print(my_str[::-1])





