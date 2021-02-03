"""
    (1-3 пункты были решены на уроке, необходимо привести все к нужному виду)
    При запуске программы выбор:
    1. Найти количество четных и нечетных цифр числа.
    2. Найти факториал числа.
    3. Вывести последовательность чисел в степени до предела.
    4. Выход.
    * после выполнения пунктов 1-3 попадаем обратно в меню.
"""

print('Меню:\n'
      '1. Найти количество четных и нечетных цифр числа.\n'
      '2. Найти факториал числа.\n'
      '3. Вывести последовательность чисел в степени до предела.\n'
      '4. Выход.')

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
