"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.
    Напишите несколько тестов для функции.
    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"
"""


def main():
    text = "hi world, hi python. i am very cool but i am still learning."
    print(frequent_word(text))


def frequent_word(text):
    word = ''
    words_list = []
    word_counter = {}

    for char in text:
        if char.isalpha():
            word += char
        elif word:
            words_list.append(word.lower())
            word = ''

    sorted_world_list = sorted(words_list)

    for word in sorted_world_list:
        if len(word) == 1:
            word = ' ' + word + ' '
        word_counter[word.replace(' ', '')] = text.count(word)

    return max(word_counter, key=word_counter.get)


if __name__ == '__main__':
    main()


text_1 = 'It is a long established fact that a reader will be ' \
      'distracted by the readable content of a page when looking at its layout.'
assert frequent_word(text_1) == 'a'

text_2 = 'It is a long established fact it a reader will be ' \
      'distracted by it readable content it a page when looking at it layout.'
assert frequent_word(text_2) == 'it'

text_2 = 'It is a long established fact it a reader will be ' \
      'distracted by it readable content it a page when looking at it layout.'
assert frequent_word(text_2) == 'it'

text_3 = 'It is a long established fact is a reader will be ' \
      'distracted by it readable content is a page when looking at is layout.'
assert frequent_word(text_3) == 'is'

print("All tests passed successfully!")
