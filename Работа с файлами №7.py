"""Напишите функцию на Python для чтения первых n строк файла."""
def file_read_from_head(filename, nlines):
    from itertools import islice
    with open(filename, 'r', encoding='utf-8') as file:
        for line in islice(file, nlines):
            print(line)
file_read_from_head('test5.txt', 1)