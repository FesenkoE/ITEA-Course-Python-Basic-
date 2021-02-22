"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).
    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
"""


def main():
    data = []
    index = 1

    with open('files/phone_book.txt', 'r') as file:
        for line in file.readlines():
            name = ''
            phone_number = ''

            for char in line:
                if char.isalpha():
                    name += char
                elif char.isdigit():
                    phone_number += char

            name = name.lower()

            if name[0] == 'm' or name[-1] == 'a':
                phone_number = '+380' + phone_number[-9:]
                data.append(str(index) + '. ' + phone_number + ' - ' + name.capitalize())
                index += 1

    with open('files/edited_phone_book.txt', 'a') as file:
        for contact in data:
            file.write(contact + '\n')


if __name__ == "__main__":
    main()
