"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input('Введите строку: ')
words = 0
longest_word = ''
symbol = True
max_len_word = 0
len_word = 0
i = 0

for char in string:

    if not char.isalpha() and symbol:
        words += 1
        symbol = False

        if len_word > max_len_word:
            max_len_word = len_word
            longest_word = string[i - max_len_word:i]

        len_word = 0
    elif char.isalpha():
        symbol = True
        len_word += 1

    i += 1

print(f'Words: {words}')
print(f'The longest word is: {longest_word} - {max_len_word}')
