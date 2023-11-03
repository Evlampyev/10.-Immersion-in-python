# 1
# Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.

# 2
# � Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# 3
# Добавьте в модуль с загадками функцию, которая принимает на вход строку
# (текст загадки) и число (номер попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения виде.
# � Для формирования результатов используйте генераторное выражение.

_tests_dict = {}


def add_test_dict(question: str, guess_number: int) -> None:
    """#3"""
    _tests_dict[question] = guess_number


def print_test_dict() -> None:
    """#3"""
    for key, item in _tests_dict.items():
        print(f"{key} - {item}")


def run_test() -> None:
    """#2"""
    tests = {
        "Зимой и летом одним цветом": ['елка', 'ёлка', 'ель'],
        "Сидит дед во сто шуб одет" : ["капуста", "лук"]
    }
    for test in tests:
        # print(test_question(test, tests[test], 5))
        guess_num = test_question(test, tests[test], 5)
        add_test_dict(test, guess_num)


def test_question(question: str, answers: list[str], guesses: int) -> int:
    """#1"""
    print(f"Загадка: {question}")
    current_guess = 1
    answers = [answer.lower() for answer in answers]

    while guesses >= current_guess:
        answer = input("Ваш ответ: ").lower()
        if answer in answers:
            return current_guess
        else:
            print("Не угадал")
        current_guess += 1
    return 0


if __name__ == '__main__':
    # print(test_question("Зимой и летом одним цветом", ['елка', 'ёлка', 'ель'], 5))
    run_test()
    print_test_dict()
