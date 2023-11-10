# Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различный случайные варианты
# и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается
# такая расстановка ферзей на шахматной доске, в которой ни один
# ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
from random import shuffle


def is_attacking(q1, q2) -> bool:
    """Проверяет, бьют ли ферзи друг друга"""
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(
            q1[1] - q2[1]):
        return True
    else:
        return False


def check_queens(queens) -> bool:
    """Проверяет все возможные пары ферзей"""
    for i in range(0, len(queens) - 1):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


def generate_boards() -> list[list[int]]:
    board_list = []
    successful_placements = 0
    count = 0
    set_queens_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    set_queens_2 = [1, 2, 3, 4, 5, 6, 7, 8]
    while successful_placements < 92:

        queens = [(set_queens_1[i], set_queens_2[i]) for i in range(0, 8)]
        count += 1
        print(count)

        if check_queens(queens):
            board_list.append(queens)
            successful_placements += 1
        shuffle(set_queens_2)
        shuffle(set_queens_1)

    return board_list


if __name__ == '__main__':
    print(generate_boards())
