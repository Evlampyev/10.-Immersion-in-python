
"""Запуск доктестов через unittest"""

from doctest import DocTestSuite, DocFileSuite
from unittest import main
import prime


def load_tests(loader, tests, ignore):
    tests.addTests(DocTestSuite(prime))  # импорт модуля prime.py для тестирования
    tests.addTests(
        DocFileSuite('doc_is_prime.md'))  # импорт документации doctest для модуля
    return tests


if __name__ == '__main__':
    main(verbosity=2)
