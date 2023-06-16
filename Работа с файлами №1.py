"""Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.
Учитывайте, что содержимое файла может быть как на русском языке, так и на английском"""
def file_read(file_name):
    with open(file_name,'r', encoding='utf-8') as file:
     content = file.read()
     print(content)

file_read('test2.txt')