"""
    Пример использования модулей random и string
    Программа выводит случайный спец-символ либо число.
    * можно делать выборку в цикле и конкатенировать все в одну строку,
    если нужно больше, чем 1 символ
"""

# from random import choice
# from string import digits, punctuation
#
#
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
