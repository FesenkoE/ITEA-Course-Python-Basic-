"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
    Программа выводит сообщение:
    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)
"""

import re
from string import digits, ascii_lowercase, ascii_uppercase


def main():
    phone = input_phone()
    email = input_email()
    pwd = input_pwd()
    print('Phone: ', phone)
    print('Email: ', email)
    print('Password: ', '*' * len(pwd))


def input_phone():
    phone = input('Enter phone number: ')
    digits_ = re.sub(r'\D', '', phone)
    phone = '+380' + digits_[-9:]

    if len(phone) != 13:
        print('Wrong format. Try again.')
        return input_phone()

    return phone


def input_email():
    email = input('Enter your email: ')

    if len(email) > 5 and email.count('@') == 1:
        return email

    print(f'Email {email} is not valid')
    return input_email()


def input_pwd():
    pwd = input('Enter your password: ')

    if len(pwd) < 8 or pwd.isspace() or not pwd_checker(pwd):
        print(f'Password {pwd} is not valid')
        return input_pwd()

    if pwd_verification(pwd):
        return pwd


def pwd_verification(pwd):
    pwd_ver = input('Confirm your password: ')

    if pwd != pwd_ver:
        input_pwd()

    return True


def pwd_checker(pwd):
    low_letter = False
    upper_letter = False
    digit_ = False

    for char in pwd:
        if char in ascii_uppercase:
            upper_letter = True
        elif char in ascii_lowercase:
            low_letter = True
        elif char in digits:
            digit_ = True

    if upper_letter and low_letter and digit_:
        return True

    return False


if __name__ == '__main__':
    main()
