# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти системы координат: '))

if number == 1:
    print(f'Возможные координаты точек в {number} четверти: x>0,y>0')
if number == 2:
    print(f'Возможные координаты точек в {number} четверти: x<0,y>0')
if number == 3:
    print(f'Возможные координаты точек в {number} четверти: x<0,y<0')
if number == 4:
    print(f'Возможные координаты точек в {number} четверти: x>0,y<0')
if number not in range (1, 5):
    print('Такой четверти нет')