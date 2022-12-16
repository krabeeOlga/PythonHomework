# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

import random
coord = []

for i in range(2):
    coord.append(random.randint(-100,101))

print(coord)

if coord[0] > 0 and coord[1] > 0:
    print('Первая четверть')
if coord[0] < 0 and coord[1] > 0:
    print('Вторая четверть')
if coord[0] < 0 and coord[1] < 0:
    print('Третья четверть')
if coord[0] > 0 and coord[1] < 0:
    print('Четвертая четверть')
if coord[0] == 0 and coord[1] != 0:
    print('Точка лежит на оси ординат')
if coord[0] != 0 and coord[1] == 0:
    print('Точка лежит на оси абсцисс')
if coord[0] == 0 and coord[1] == 0:
    print('Точка лежит в начале системы координат')
