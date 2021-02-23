"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def main():
    ticket_num = 1230
    if is_lucky(ticket_num):
        print('The ticket is lucky')
    else:
        print('The ticket is unlucky')


def is_lucky(ticket_num):
    num_list = list(str(ticket_num))
    first_sum = None
    second_sum = None

    if len(num_list) % 2 == 0:
        half_list = len(num_list) // 2
        first_sum = sum(list(map(int, num_list[:half_list])))
        second_sum = sum(list(map(int, num_list[half_list:])))

    if first_sum == second_sum:
        return True

    return False


if __name__ == '__main__':
    main()





assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print("All tests passed successfully!")