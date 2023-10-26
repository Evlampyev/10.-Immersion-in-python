#  Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.


def method_without_count(text: str) -> None:
    my_dict = {}
    for letter in text:
        if letter.isalpha():  # Если это буквы
            my_dict[letter] = my_dict.get(letter, 0) + 1
            # get ищет ключ, если его нет возвращает 0
    print(my_dict)


def method_with_count(text):
    my_dict = {}
    for el in set(text):  # отобрали только уникальные значения
        if el.isalpha():
            if el not in my_dict:
                my_dict[el] = text.count(el)
    print(my_dict)


my_text = (
    'Пользователь вводит строку текста. Подсчитайте сколько раз встречается '
    'каждая буква в строке без использования метода count и с ним.')

method_without_count(my_text)
method_with_count(my_text)
