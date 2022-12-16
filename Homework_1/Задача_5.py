# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import random
coord1 = []

for i in range(2):
    coord1.append(random.randint(-100, 101))

print(coord1)

coord2 = []

for i in range(2):
    coord2.append(random.randint(-100,101))

print(coord2)

distance = round(((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2)**(0.5), 2)

print(distance)