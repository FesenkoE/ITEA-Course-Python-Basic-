"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:
    1. Все сгенерированные пароли записывались в файл.
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".
    *3. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.
    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается
"""

from random import choice, randint
from string import digits, punctuation, ascii_lowercase, ascii_letters, hexdigits, ascii_uppercase


def main():
    print('1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)\n'
          '2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)\n'
          '3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ,'
          'длина от 8 до 16 символов)')

    choice_ = input('Выберите один из 3-х вариантов: ')

    if choice_ == '1':
        pwd = simple_pwd()
        with open('files/pwd.txt', 'a+') as file:
            file.write(pwd + '\n')
        print(pwd)
    elif choice_ == '2':
        pwd = middle_pwd()
        with open('files/pwd.txt', 'a+') as file:
            file.write(pwd + '\n')
        print(pwd)
    elif choice_ == '3':
        pwd = difficult_pwd()
        with open('files/pwd.txt', 'a+') as file:
            file.write(pwd + '\n')
        print(pwd)


def simple_pwd():
    pwd = ''
    for char in range(8):
        pwd += choice(ascii_lowercase)

    with open('files/pwd.txt', 'r') as file:
        if pwd in file.readlines():
            print('Insecure password')

    return pwd


def middle_pwd():
    pwd = ''
    string = ascii_letters + digits
    for char in range(8):
        pwd += choice(string)

    with open('files/pwd.txt', 'r') as file:
        if pwd in file.readlines():
            print('Insecure password')

    return pwd


def difficult_pwd():
    pwd = ''
    string = hexdigits + punctuation
    len_pwd = randint(8, 16)

    for char in range(len_pwd):
        pwd += choice(string)

    if not pwd_checker(pwd):
        return difficult_pwd()

    with open('files/pwd.txt', 'r') as file:
        if pwd in file.readlines():
            print('Insecure password')

    return pwd


def pwd_checker(pwd):
    low_letter = False
    upper_letter = False
    digit_ = False
    special_char = False

    for char in pwd:
        if char in ascii_uppercase:
            upper_letter = True
        elif char in ascii_lowercase:
            low_letter = True
        elif char in digits:
            digit_ = True
        elif char in punctuation:
            special_char = True

    if upper_letter and low_letter and digit_ and special_char:
        return True

    return False


if __name__ == '__main__':
    main()
