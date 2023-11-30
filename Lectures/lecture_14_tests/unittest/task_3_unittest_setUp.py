from unittest import main, TestCase


class TestSample(TestCase):
    def setUp(self) -> None:
        """Перед каждым тестом создаёт новый список"""
        self.data = [2, 3, 5, 7]
        print('Выполнил setUp')  # Только для демонстрации работы метода

    def test_append(self):
        self.data.append(11)
        self.assertEqual(self.data, [2, 3, 5, 7, 11])

    def test_remove(self):
        self.data.remove(5)  # удаление значения 5 из исходного списка
        self.assertEqual(self.data, [2, 3, 7])

    def test_pop(self):
        self.data.pop()  # удаление последнего элемента из исходного списка
        self.assertEqual(self.data, [2, 3, 5])


if __name__ == '__main__':
    main()
