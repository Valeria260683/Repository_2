"""Напишите функцию на Python для чтения всего текстового файла"""

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

filename = 'test4.txt'
text = read_file(filename)
print(text)