"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.
    2. Релизовать функцию grouping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""


def main():
    data = {
        "Ukraine": ["Kiev", "Kharkov", "Odessa", "Dnipro"],
        "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
        "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
        "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
    }

    # print(get_country("Berlin"))
    print(grouping_data(data))


def get_country(city):
    data = {
        "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
        "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
        "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
        "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
    }

    for country in data:
        if city in data[country]:
            return country

    return False


def grouping_data(data):
    group_data = []

    for country in data:
        group_data.append({
            "country": country,
            "capital": data[country][0],
            "cities": data[country]
        })

    return group_data


if __name__ == '__main__':
    main()
