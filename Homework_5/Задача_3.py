# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

from random import randint as RI
import os

def read_file(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), "r")
    return f.read()

def write_file(filename, value):
    f = open(os.path.join(os.path.dirname(__file__), filename), "w")
    f.write(value)
    f.close()

def rle(data):
    if str(data)[0].isalpha():
        return zip(data)
    else:
        return restore(data)

def zip(data):
    print(f'zip {data} -> ', end='')
    result = ''
    old = ''
    count = 1
    for symbol in data:
        if symbol != old:
            if old:
                result += str(count) + old
            count = 1
            old = symbol
        else:
            count += 1
    result += str(count) + old

    print(result)
    return result

def restore(data):
    print(f'restore {data} -> ', end='')
    count = 0
    result = ''

    for symbol in str(data):
        if symbol.isalpha():
            for i in range(count):
                result += symbol
        else:
            count = int(symbol)
    print(result)
    return result

rle_restore = read_file("task3-in")
write_file("task3-out", rle(rle_restore))

rle_zip = read_file("task3-out")
write_file("task3-in", rle(rle_zip))
