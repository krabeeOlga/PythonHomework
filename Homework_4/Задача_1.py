# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random 

def create_my_dict():
    my_dict = {}
    n = int(input('Введите максимальную степень: '))
    for i in range(n, -1, -1):
        if i == n:
            while True:
                koef = random.randint(0, 100)
                if koef != 0:
                    break
                # else:
                #     print('Был 0')
            my_dict[i] = koef
        else:
            my_dict[i] = random.randint(0, 100)
    return my_dict

def get_equation(my_dict1):
    equation =''
    for item in my_dict1:
        value = ''
        if(my_dict1[item] == 0):
            continue    
        if(my_dict1[item] == 1):
            value = ''
        else:
            value = str(my_dict1[item])

        x = ''
        if(item == 0 and my_dict1[item] == 1):
            x = '1'
        elif(item == 0):
            x = ''
        elif(item == 1):
            x = 'x'
        elif(my_dict1[item] == 1):
             x = 'x**' + str(item)
        else:
            x = '*x**' + str(item)
        
        if(equation != ''):
            equation = equation + ' + ' + value + x
        else: 
            equation = value + x
        print(equation)
    equation = equation + ' = 0'
    return equation

def write_file(filename, value):
    f = open(filename, "w")
    f.write(value)
    f.close()

#equation1
my_dict1 = create_my_dict()
print(str(my_dict1))
equation = get_equation(my_dict1)
print(equation)
write_file("equation1", equation)

#equation2
my_dict1 = create_my_dict()
print(str(my_dict1))
equation = get_equation(my_dict1)
print(equation)
write_file("equation2", equation)




