from unittest import main, TestCase


class TestSample(TestCase):
    def setUp(self) -> None:
        """Создаёт перед каждым тестом файл со строками чисел"""
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')

    def test_line(self):
        """Проверили что строчек в файле 10"""
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
        self.assertEqual(i, 10)

    def test_first(self):
        """Проверили, что первые 5 цифр - 00000"""
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
            self.assertEqual(first, '00000')

    def tearDown(self) -> None:
        """Удаляет файл созданный в setUp после каждого теста"""
        from pathlib import Path
        Path('top_secret.txt').unlink()


if __name__ == '__main__':
    main()
