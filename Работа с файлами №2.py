"""Напишите функцию file_n_lines, которая печатает первые n-строка файла. Функция file_n_lines
принимает на вход название файла и количество строк для прочтения.
Не забывайте избавляться от символа переноса строки
К примеру, если бы имелся файл hello.txt со следующим содержимым:

h
he
hel
hell
hello
То вызов file_n_lines(hello.txt, 3) должен распечатать следующее:

h
he
hel
Ваша задача написать только определение функции file_n_lines"""
def file_n_lines(file_name, n):
    with open(file_name,'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(n):
            line = lines[i].rstrip() # избавляемся от символа переноса строки
            print(line)
file_n_lines('hello.txt', 3)