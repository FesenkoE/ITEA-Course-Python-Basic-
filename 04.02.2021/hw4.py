"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

# string = input('Введите строку: ')
# words = 0
# longest_word = ''
# symbol = True
# max_len_word = 0
# len_word = 0
# i = 0
#
# for char in string:
#
#     if not char.isalpha() and symbol:
#         words += 1
#         symbol = False
#
#         if len_word > max_len_word:
#             max_len_word = len_word
#             longest_word = string[i - max_len_word:i]
#
#         len_word = 0
#     elif char.isalpha():
#         symbol = True
#         len_word += 1
#
#     i += 1
#
# print(f'Words: {words}')
# print(f'The longest word is: {longest_word} - {max_len_word}')


"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.
    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)
    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))
    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""

# можно заменить данную строку на input()
# string = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.'

# lower_symbols = 0
# upper_symbols = 0
# is_capitalize_word = True
# word = ''
# symbol = True
# result = ''
#
# for char in string:
#     if char.islower():
#         lower_symbols += 1
#     elif char.isupper():
#         upper_symbols += 1
#
#     if not char.isalpha() and symbol:
#         if word[0].islower():
#             is_capitalize_word = False
#         symbol = False
#         word = ''
#     elif char.isalpha():
#         word += char
#         symbol = True
#
# if lower_symbols > upper_symbols:
#     string = string.lower()
# elif lower_symbols < upper_symbols:
#     string = string.upper()
# else:
#     string = string.swapcase()
#
# if is_capitalize_word:
#     result = 'done. ' + string
# else:
#     result = 'draft. ' + string[6:]
#
# if len(result) > 20:
#     result = result[:21]
# else:
#     count_additional_symbols = 20 - len(result)
#     result = result + count_additional_symbols * '@'
#
#
# print(f'Исходня строка: {string}\n'
#       f'Результат: {result}')


"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.
    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""
digits = 0
phone_number = ''

while True:
    phone = input('Enter phone number: ')

    for symbol in phone:
        if symbol.isdigit():
            phone_number += symbol

    digits = len(phone_number)

    if 8 < digits < 13:
        if digits == 9:
            phone_number = '380' + phone_number
        elif digits == 10:
            phone_number = '38' + phone_number
        elif digits == 11:
            phone_number = '3' + phone_number

        print(phone_number)
        break

"""
 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'


 2. Найти индекс самой последней буквы 's' в строке.
    Результат: 53


 3. Найти количество букв 'i' в строке (регистр не имеет значения).
    Результат: 6


 4. Найти и вывести срез строки.
    Результат: 'simply dummy text'
    (используйте методы find или index для получения индексов)


 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
    и выведите на экран.
    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'
"""

# string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1.
# string = string.replace(', ', ' ')
# print(string)

# 2.
# find_index = string.rfind('s')
# print(find_index)

# 3.
# i_count = string.count('i') + string.count('I')
# print(i_count)

# 4.
# find_text = 'simply dummy text'
# find_index = string.find(find_text)
# print(string[find_index:find_index + int(len(find_text))])

# 5.
# first_string_part = string[:len(string) // 2]
# string = first_string_part * 3 + string[len(string) // 2:]
# print(f'Результат: {string}')
