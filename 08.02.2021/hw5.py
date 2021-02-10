"""
    Пример использования модулей random и string
    Программа выводит случайный спец-символ либо число.
    * можно делать выборку в цикле и конкатенировать все в одну строку,
    если нужно больше, чем 1 символ
"""

from random import choice, randint
from string import digits, punctuation, ascii_lowercase, ascii_letters, hexdigits, ascii_uppercase

# def main():
#     # генерируем строку для выборки
#     tmp = digits + punctuation
#     print(f'Digits: {digits}')
#     print(f'Punctuation: {punctuation}')
#
#     # выбираем случайный символ из строки
#     char = choice(tmp)
#
#     print(char)
#
#
# main()

"""
    Пример использования рекурсии для формы регистрации.
    Допустим программа задает вопрос: Сколько будет 2 + 2?
    до тех пор, пока не получит правильный ответ,
    после чего выводит сообщение "Верно, 4!".
"""

# def main():
#     answer = get_answer()
#     print(f'Верно, {answer}!')
#
#
# def get_answer():
#     answer = input('Сколько будет 2 + 2? ')
#     if answer != '4':
#         return get_answer()
#     return answer
#
#
# main()

"""
    Данную программу можно модифицировать, и для удобства пользователя
    выводить сообщение при неверном ответе.
"""

# def main():
#     answer = get_answer()
#     print(f'Верно, {answer}!')


# def get_answer():
#     answer = input('Сколько будет 2 + 2? ')
#     if answer != '4':
#         print('Неверно! Попробуйте еще раз.')
#         return get_answer()
#     return answer
#
#
# main()

# еще один вариант, с параментром функции
# def get_answer(question='Сколько будет 2 + 2? '):
#     answer = input(question)
#     if answer != '4':
#         return get_answer('Неверно! Попробуйте еще раз.\nСколько будет 2 + 2?')
#     return answer
#
#
# main()

"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, 
    длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501

"""Обсудить на уроке
Вопрос - Возвращает не последний результат, а первый
"""


def main():
    print('1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)\n'
          '2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)\n'
          '3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ,'
          'длина от 8 до 16 символов)')

    choice_ = input('Выберите один из 3-х вариантов: ')

    if choice_ == '1':
        print(simple_pwd())
    elif choice_ == '2':
        print(middle_pwd())
    elif choice_ == '3':
        print(difficult_pwd())


def simple_pwd():
    pwd = ''
    for char in range(8):
        pwd += choice(ascii_lowercase)

    return pwd


def middle_pwd():
    pwd = ''
    string = ascii_letters + digits
    for char in range(8):
        pwd += choice(string)

    return pwd


def difficult_pwd():
    pwd = ''
    string = hexdigits + punctuation
    len_pwd = randint(8, 16)

    for char in range(len_pwd):
        pwd += choice(string)

    print(f'Before check: {pwd}')
    if not pwd_checker(pwd):
        difficult_pwd()

    print(f'Finished result: {pwd}')
    return pwd


def pwd_checker(pwd):
    low_letter = False
    upper_letter = False
    digit_ = False
    special_char = False

    for char in pwd:
        if char in ascii_uppercase:
            upper_letter = True
            print(f'upper_letter: {char}')
        elif char in ascii_lowercase:
            low_letter = True
            print(f'low_letter: {char}')
        elif char in digits:
            digit_ = True
            print(f'digit_: {char}')
        elif char in punctuation:
            special_char = True
            print(f'special_char: {char}')

    if upper_letter and low_letter and digit_ and special_char:
        print('success')
        return True

    print('Fail')
    return False


if __name__ == '__main__':
    main()
