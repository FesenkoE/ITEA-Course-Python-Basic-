"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.
    1. При запуске, программа спрашивает имя игрока.
    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру
    3. При выходе из программы данные игрока записывать в файл (txt либо json).
    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.
"""
import random
import json


def main():
    player_data = {
        'name': '',
        'games': 0,
        'record': 0,
        'avg_attempts': 0
    }
    user_name = input('Enter your name: ')
    player_data['name'] = user_name
    random_number = random.randint(1, 100)

    var = True
    attempt = 0

    while var:
        number = int(input('Enter a number: '))
        attempt += 1

        if number < random_number:
            print('Number is less than Magic Number')
        elif number > random_number:
            print('Number is more than Magic Number')
        else:
            print('You guessed Magic Number: ', random_number, '\nYour attempt is: ', attempt)

            answer = input('Continue? (Y/n): ')
            player_data['games'] += 1

            if player_data['record'] == 0 or player_data['record'] > attempt:
                player_data['record'] = attempt

            player_data['avg_attempts'] = (player_data['avg_attempts'] + attempt) / player_data['games']
            attempt = 0
            random_number = random.randint(1, 100)

            if answer == 'n':
                var = False
                with open('files/player_data.txt', 'w') as file:
                    json.dump(player_data, file)


if __name__ == '__main__':
    main()
