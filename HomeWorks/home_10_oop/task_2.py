class LotteryGame:
    def __init__(self, lst_1: list, lst_2: list):
        self.list_1 = lst_1
        self.list_2 = lst_2

    def compare_lists(self):
        set_1 = set(self.list_1)
        set_2 = set(self.list_2)
        result = set_1 & set_2
        if len(result) == 0:
            print("Совпадающих чисел нет.")
        else:
            print(f'Совпадающие числа: {list(result)} \n'
                  f'Количество совпадающих чисел: {len(result)}')


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
