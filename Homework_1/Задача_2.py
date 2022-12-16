# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

my_list = []
for i in range(3):
    my_list.append(int(input(f'Введите {i+1} значение: ')))

a = not (my_list[0] or my_list[1] or my_list[2])
b = not my_list[0] and not my_list[1] and not my_list[2]

if a == b:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")

