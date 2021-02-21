"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""

"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""


def main():
    with open('files/file_practice.txt', 'w+') as file:
        file.write('Starting practice with files\n')
        file.seek(0)
        first_five_symbols = file.read(5)
        # print(f'First five symbols: {first_five_symbols}\n')

        with open('files/text.txt', 'r') as text:
            old_text = text.read()
            count_i = old_text.count('i')
            count_e = old_text.count('e')

            if count_i > count_e:
                new_text = old_text.replace('i', 'e')
            elif count_i < count_e:
                new_text = old_text.replace('e', 'i')
            else:
                new_text = old_text

            file.write(new_text + '\n')

            file_content = read_full(file)

            if len(file_content) % 2 == 0:
                file.write('the end')
            else:
                file.write('bye')

            file_content = read_full(file)
            print(f'new file:\n{file_content}')

            half_of_text = len(file_content) // 2
            inserted_text = ' *some inserted text* '
            new_file_content = file_content[:154] + inserted_text + file_content[154 + len(inserted_text):]

            file.seek(0)
            file.write(new_file_content)


def read_full(file):
    file.seek(0)
    return file.read()


if __name__ == '__main__':
    main()
