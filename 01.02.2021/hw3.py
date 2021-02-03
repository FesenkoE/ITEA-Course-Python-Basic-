"""
    (1-3 пункты были решены на уроке, необходимо привести все к нужному виду)
    При запуске программы выбор:
    1. Найти количество четных и нечетных цифр числа.
    2. Найти факториал числа.
    3. Вывести последовательность чисел в степени до предела.
    4. Выход.
    * после выполнения пунктов 1-3 попадаем обратно в меню.
"""

# print('Меню:\n'
#       '1. Найти количество четных и нечетных цифр числа.\n'
#       '2. Найти факториал числа.\n'
#       '3. Вывести последовательность чисел в степени до предела.\n'
#       '4. Выход.')

# var = True
#
# while var:
#     try:
#         answer = int(input('Сделайте выбор и нажмите Enter: '))
#
#         if answer == 1:
#             number = int(input("Введите число: "))
#             biggest = 0
#             even = 0
#             odd = 0
#
#             while number > 0:
#                 last_digit = number % 10
#
#                 if last_digit % 2 == 0:
#                     even += 1
#                 else:
#                     odd += 1
#
#                 if last_digit > biggest:
#                     biggest = last_digit
#
#                 number //= 10
#
#             print("biggest:", biggest)
#             print("even:", even)
#             print("odd:", odd)
#
#             break
#         elif answer == 2:
#             number = int(input("Введите число: "))
#
#             factorial = 1
#             while number > 1:
#                 factorial *= number
#                 number -= 1
#
#             print(factorial)
#
#             break
#         elif answer == 3:
#             p = int(input("Введите степень: "))
#             limit = int(input("Предел: "))
#             number = 1
#
#             while (result := number ** p) < limit:
#                 print(result)
#                 number += 1
#             break
#         elif answer == 4:
#             print('Bye!')
#
#             break
#         else:
#             print('You entered wrong number')
#     except ValueError:
#         print('You entered wrong number')


"""
    Алгоритм Евклида. НОД - наибольший общий делитель
    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (выходим из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.
"""

# a = int(input('Enter number a: '))
# b = int(input('Enter number b: '))

# try:
#     a = int(input('Enter number a: '))
#     b = int(input('Enter number b: '))
#
#     if a > 0 and b > 0:
#         while a != 0 and b != 0:
#             if a > b:
#                 a = a % b
#             else:
#                 b = b % a
#
#         print('nod: ', a) if a != 0 else print('nod: ', b)
#     else:
#         print('Numbers should be positive')
# except ValueError:
#     print('Invalid literal')


"""
    Магическое число.
    Необходимо угадать загаданное число за наименьшее количество попыток.
    Алгоритм:
    1. Генерируется случайное число.
    2. Пользователь вводит число.
    3. Если введенное число больше или меньше сгенерированного, то
        выводится соответствующее сообщение и возвращаемся к пункту 2.
    4. Иначе введенное число равняется сгенерированному -
        пользователь угадал число. Выводится само число и количество попыток.
        А так же вопрос "Continue? (Y/n) ".
    6. Если пользователь выбирает продолжить -
        обнуляем счетчик попыток и переходим к пункту 1.
    7. Иначе выводим сообщение 'Bye!'.
    * Для генерации случайного числа используем random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел
    ** по желанию, можете хранить рекордное число попыток
    и сообщать пользователю, если он поставил новый рекорд
"""

# import random
#
# random_number = random.randint(1, 100)  # случайное число от 1 до 100
#
# var = True
# attempt = 0
#
# while var:
#     number = int(input('Enter a number: '))
#     attempt += 1
#
#     if number < random_number:
#         print('Number is less than Magic Number')
#     elif number > random_number:
#         print('Number is more than Magic Number')
#     else:
#         print('You guessed Magic Number: ', random_number, '\nYour attempt is: ', attempt)
#         attempt = 0
#
#         answer = input('Continue? (Y/n): ')
#         if answer == 'n':
#             var = False


"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""
# try_again = True
#
# while try_again:
#     try:
#         n = int(input('Enter a number: '))
#         op = input('Enter an operation (+, -, *, /): ')
#         n_numbers = int(input('Enter N of numbers: '))
#         n_add = n
#         is_result = True
#
#         for i in range(1, n_numbers):
#             if op == '+':
#                 n += n_add
#             elif op == '-':
#                 n -= n_add
#             elif op == '*':
#                 n *= n_add
#             elif op == '/':
#                 n /= n_add
#             else:
#                 print('You entered wrong operation: ', op)
#                 is_result = False
#                 break
#
#         if is_result:
#             print('Result is: ', n)
#             is_continue = input('Continue? (Y/n): ')
#             if is_continue == 'n':
#                 try_again = False
#
#     except ValueError:
#         print('invalid literal ')


"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.
    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение не четных чисел числового ряда.
    * обработать возможные ошибки
"""

# try:
#     start = int(input('Enter start: ') or 0)
#     end = int(input('Enter end: '))
#     sum_ = 0
#     prod_of_num = 1
#
#     for i in range(start, end):
#         sum_ += i
#
#         if i % 2 != 0:
#             prod_of_num *= i
#
#     print('Sum: ', sum_, '\nProduct of numbers: ', prod_of_num)
# except ValueError:
#     print('Start or End are wrong')
