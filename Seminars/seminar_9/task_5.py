# 📌Объедините функции из прошлых задач.
# 📌Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌Выберите верный порядок декораторов.
from task_2 import ugadaika_decorator
from task_3 import decorator_save_to_json
from task_4 import count_calls


@count_calls(2)
@ugadaika_decorator
@decorator_save_to_json
def func_ugadaika(user_guess: int, user_num: int) -> str:
    """
    Угадываем число за указанное количество попыток
    :param user_guess: количество попыток
    :param user_num: загаданное число
    :return: результат угадывания
    """
    current_guess = 1
    while current_guess <= user_guess:
        ans = int(input(f"Попытка №{current_guess}. Ваш вариант: "))
        if ans > user_num:
            print('Меньше')
        elif ans < user_num:
            print("Больше")
        else:
            return f"Вы угадали на {current_guess} попытке. "
        current_guess += 1
    else:
        return f'Ваши попытки закончились. Вы проиграли. Ответ {user_num}.'


if __name__ == '__main__':
    play = func_ugadaika(12, 49)
    print(play)


# необходимо немножко подправить файлы для более правильного вывода, там с return проблемы
