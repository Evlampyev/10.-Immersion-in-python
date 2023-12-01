# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

from unittest import main, TestCase
from Seminars.seminar_12_oop_end.task_4 import Rectangle


class RectangleTest(TestCase):
    def setUp(self):
        self.test_rectangle = Rectangle(12, 6)
        self.test_square = Rectangle(4)

    def test_rect_creation(self):
        self.assertEqual(self.test_rectangle, Rectangle(12, 6))

    def test_square_creation(self):
        self.assertEqual(self.test_square, Rectangle(4))

    def test_addition(self):
        self.assertEqual(self.test_rectangle + self.test_rectangle, Rectangle(24, 12))

    def test_compare(self):
        self.assertTrue(self.test_rectangle, self.test_square)

    def test_exception(self):
        """Проверка на отлов ошибки ValueError при создании"""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-1, 1)


if __name__ == '__main__':
    main()
