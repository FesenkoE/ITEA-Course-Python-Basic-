# 1. Создайте переменную x, которая равняется 2 в степени 3


# 2. Прибавьте к x 3


# 3. Сгенерируйте список num_list длиной x, из случайных чисел от 1 до x


# 4. Выведите на экран числа из списка num_list в обратном порядке
#    (от последнего до первого элемента) через пробел


# 5. Вставьте в средину списка число 11.


# 6. Запишите в файл list_info.txt строчки
#    - 1. количество элементом списка num_list
#    - 2. количество уникальных элементов списка num_list
#    - 3. самое маленькое число списка num_list
#    - 4. сумму чисел списка num_list кратных 3


# 7. Отсортируйте список словарей countries_info
#    по ключу 'population' в порядке возрастания,
#    а также каждый список cities по длине строк в порядке убывания
countries_info = [
    {
        "country": "Ukraine",
        "population": 42000000,
        "cities": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    },
    {
        "country": "France",
        "population": 66999999,
        "cities": ["Paris", "Marseille", "Lyon", "Toulouse"],
    },
    {
        "country": "Germany",
        "population": 83000000,
        "cities": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
    },
]


# 8. Напишите функцию create_country_info, которая принимает параметры
#     country, population, cities и возвращает словарь


# 9. Создайте словарь с помощью функции create_country_info
#     и вставьте его в начало списка countries_info


# 10. Создать репозиторий и залить туда этот файл

def main():
    x = pow(2, 3)
    print(x)


if __name__ == '__main__':
    main()
