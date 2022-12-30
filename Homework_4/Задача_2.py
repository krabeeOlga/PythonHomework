# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random, os

def read_file(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), "r")
    return f.read()

def write_file(filename, value):
    f = open(os.path.join(os.path.dirname(__file__), filename), "w")
    f.write(value)
    f.close()

def parse_equation(string: str):
    eq = {}
    my_list = string.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -').split()

    for item in my_list:
        x = 0
        value = 1
        if item.startswith('x'):
            x = 1
        elif item.startswith('-x'):
            x = 1
        else:
            if "**" in item: 
                x = int(item.split('**')[1]) #степень
            elif "x" in item:
                x = 1
            value = int(item.split('*x')[0])
        eq[x] = value
    # print(eq)
    return eq

def summa_equations(eq1, eq2):
    n = len(eq1)
    if(len(eq1) < len(eq2)):
        n = len(eq2)

    result_list = {}
    for i in range(n -1, -1, -1):
        a = 0
        b = 0
        if(i in eq1):
            a = eq1[i]
        if(i in eq2):
            b = eq2[i]
        result_list[i] = a + b
    # print(result_list)
    return result_list

def get_equation(my_dict):
    equation =''
    for item in my_dict:
        value = ''
        if(my_dict[item] == 0):
            continue    
        if(my_dict[item] == 1):
            value = ''
        else:
            value = str(my_dict[item])

        x = ''
        if(item == 0 and my_dict[item] == 1):
            x = '1'
        elif(item == 0):
            x = ''
        elif(item == 1 and my_dict[item] != 1):
            x = '*x'
        elif(item == 1):
            x = 'x'
        elif(my_dict[item] == 1):
             x = 'x**' + str(item)
        else:
            x = '*x**' + str(item)
        
        if(equation != ''):
            equation = equation + ' + ' + value + x
        else: 
            equation = value + x
    equation = equation + ' = 0'    
    print(equation)    
    return equation

str1 = read_file("equation1")
print(str1)
eq1 = parse_equation(str1)

str2 = read_file("equation2")
print(str2)
eq2 = parse_equation(str2)

summa_eq = summa_equations(eq1, eq2)
result = get_equation(summa_eq)

write_file("equation_result", result)