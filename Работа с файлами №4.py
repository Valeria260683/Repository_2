"""Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого
находит самое длинное слово и возвращает его в качестве ответа. В случае,  если есть несколько
слов с максимальной длиной, нужно вернуть слово, которое встречается последнее в тексте.
При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации
необходимо исключить.  И также учитывайте, что слова в тестах будут как на русском языке,
так и на английском.
Если бы содержимое файла было таким:
He was running, but it was like running through deep water. There were trees all around him,
trees which tried to stop him. They reached out with their branches.
And it was behind him. It was coming nearer.
то ответом было бы слово branches
Все возможные знаки пунктуации можно получить из модуля string
from string import punctuation"""

from string import punctuation   # импортируем необходимую переменную из модуля
def remove_punctuations(word):   # создаем функцию удаления знаков пунктуации
    for punct in punctuation:    # проходимся по переменной в которой хранятся все знаки пунктуации
        if punct in word:        # если этот знак есть в нашем слове
            word = word.replace(punct, "")# удаляем этот знак
    return word                  # возвращаем слово без знаков препинания
def longest_word_in_file(file_name):
    file = open(file_name, "r", encoding="utf-8")# открываем файл
    max_word = ""                # создаем переменную для хранения самого длинного слова
    for line in file:            # циклом проходимся по файлу
        words = line.split()     # разбиваем строку на список со словами из строки
        for word in words:       # проходимся по данному списку
            word_without_punct = remove_punctuations(word) # удаляем знаки пунктуации
            if len(word_without_punct) >= len(max_word):   # если длина встречающегося слова больше или
                max_word = word_without_punct  # равна слова сохраненного в переменной с самым длинным словом
    file.close()                               # то это слово записываем в переменную
    return max_word
print(longest_word_in_file('test3.txt'))
