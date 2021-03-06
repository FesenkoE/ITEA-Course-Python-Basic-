"""
    Ввести с помощью input() 3 числа.
    Вывести их с помощью print() в обратном порядке.
    Пример работы программы:
    Ввод:
    1
    125
    13
    Вывод:
    13
    125
    1
"""
# print('Ввод:')
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
# print('Вывод: ', number_3, number_2, number_1, sep='\n')

"""
    Программа принимает на ввод 4 числа.
    Необходимо сложить первые два и отдельно вторые два.
    Разделить первую сумму на вторую.
    Вывести результат на экран.
"""

# для получения числа с помощью input() используйте такую конструкцию
# a = int(input('Enter number a: '))
# b = int(input('Enter number b: '))
# c = int(input('Enter number c: '))
# d = int(input('Enter number d: '))
#
# result = int(((a + b) / (c + d)))
# print(result)

"""
    Объявить переменные name, age, city,
    присвоив им значения с помощью input().
    Вывести на экран текст типа:
    Max from Kiev
    He is 21
"""

# name = input('Enter name: ')
# age = input('Enter age: ')
# city = input('Enter city: ')
#
# print(name + ' from ' + city, 'He is ' + age, sep='\n')

"""
    Вывести периметр и площадь прямоугольника.
    Стороны прямоугольника вводятся с помощью input().
    Периметр - сумма всех сторон прямоугольника (удвоенная сумма 2х сторон)
    Площадь - произведение 2х сторон прямоугольника.
"""

# a = int(input('Введите сторону a: '))
# b = int(input('Введите сторону b: '))
#
# print('Периметр прямоугольника: ' + str((a + b)*2))
# print('Площадь прямоугольника: ' + str((a * b)))

"""
    Вывести площадь и периметр прямоугольного треугольника.
    Катеты вводятся с помощью input().
    Площадь - произведение катетов деленное на 2.
    Периметр - сумма 3х сторон треугольника.
    * используйте теорему Пифагора: c ** 2 == a ** 2 + b ** 2
    * чтоб взять квадратный корень достаточно возвести в степень 0.5
"""

a = int(input('Катет a: '))
b = int(input('Катет b: '))
c = (a ** 2 + b ** 2) ** 0.5

square = (a * b) / 2
perimeter = a + b + c

print("Площадь треугольника: " + str(square))
print("Периметр треугольника: " + str(perimeter))
