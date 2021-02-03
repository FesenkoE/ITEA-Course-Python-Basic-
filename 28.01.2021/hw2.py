"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.
    В зависимости от введенного оператора,
    между числами проводится определенная операция.
    Результат выводится на экран.
    * обработать все возможные ошибки программы с помощью try-except
"""

# result = ''
#
# try:
#     number_a = float(input('Enter number a: '))
#     operation = input('select an option (+ - * / ): ')
#     number_b = float(input('Enter number b: '))
#
#     if operation == '+':
#         result = number_a + number_b
#     elif operation == '-':
#         result = number_a - number_b
#     elif operation == '*':
#         result = number_a * number_b
#     elif operation == '/':
#         result = number_a / number_b
#     else:
#         result = 'You selected incorrect option!'
#
# except ZeroDivisionError:
#     print('Division by zero')
# except ValueError:
#     print('You entered not a number!')
#
# if result:
#     print('Result: ', result)

"""
    Вводится год.
    Программа выводит количество дней в году, учитывая високосный год.
    * високосный год кратный 4, но не кратный 100 или кратный 400
"""

# try:
#     year = abs(int(input('Enter the Year: ')))
#
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('%d - this is a leap year (366 days)' % year)
#     else:
#         print('%d - this is not a leap year (365 days)' % year)
# except ValueError:
#     print('You entered an incorrect year')

"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)
    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""

# sum_ = 0
#
# try:
#     number = int(input('Enter number from 1 to 999: '))
#
#     if 0 < number < 1000:
#         if 0 < number < 10:
#             sum_ = number
#
#             print('Summa is: ', sum_)
#         elif 9 < number < 100:
#             number_1 = number // 10
#             number_2 = number % 10
#             sum_ = number_1 + number_2
#
#             print('Summa of numbers '
#                   + str(number_1) + ' + '
#                   + str(number_2) + ' = ', sum_)
#         else:
#             number_1 = number // 100
#             number_2 = number % 100 // 10
#             number_3 = number % 10
#
#             sum_ = number_1 + number_2 + number_3
#
#             print('Summa of numbers '
#                   + str(number_1) + ' + '
#                   + str(number_2) + ' + '
#                   + str(number_3) + ' = ', sum_)
#     else:
#         print('the number is not in range')
# except ValueError:
#     print('You entered not a number or float number!')

"""
    Программа принимает на ввод координаты точки - x и y.
    Выводит, в какой четверти системы координат лежит точка.
                ^ y
                |
            II  |    I
                |
        --------=-------->
                |         x
            III |    IV
                |
"""
# try:
#     x = float(input('Enter x: '))
#     y = float(input('Enter y: '))
#
#     if x > 0 and y > 0:
#         print('Point (%s; %s) is in I quarter coordinate system' % (x, y))
#     elif x == 0 and y > 0:
#         print('Point (%s; %s) is in I and II quarters coordinate system' % (x, y))
#     elif x < 0 and y > 0:
#         print('Point (%s; %s) is in II quarter coordinate system' % (x, y))
#     elif x < 0 and y == 0:
#         print('Point (%s; %s) is in II and III quarters coordinate system' % (x, y))
#     elif x < 0 and y < 0:
#         print('Point (%s; %s) is in III quarter coordinate system' % (x, y))
#     elif x == 0 and y < 0:
#         print('Point (%s; %s) is in III and IV quarters coordinate system' % (x, y))
#     elif x > 0 and y < 0:
#         print('Point (%s; %s) is in IV quarter coordinate system' % (x, y))
#     elif x > 0 and y == 0:
#         print('Point (%s; %s) is in IV and I quarters coordinate system' % (x, y))
#     else:
#         print('The point (%s; %s) is in the beginning of coordinate system' % (x, y))
# except ValueError:
#     print('You entered not a number')

"""
    Определить, существует ли треугольник.
    Программа принимает на ввод 3 стороны треугольника.
    Выводит стороны и текст, существует треугольник или нет.
    * у треугольника каждая сторона меньше суммы двух других сторон
"""
try:
    side_a = float(input('Enter side A: '))
    side_b = float(input('Enter side B: '))
    side_c = float(input('Enter side C: '))

    if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
        print('Triangle with sides: \nSide A: %s \nSide B: %s \nSide C: %s exists' % (side_a, side_b, side_c))
    else:
        print('Triangle with sides: \nSide A: %s \nSide B: %s \nSide C: %s does not exist' % (side_a, side_b, side_c))
except ValueError:
    print('You entered not a number')
