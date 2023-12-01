from pytest import main, raises
from prime_pytest import is_prime


def test_is_prime():
    assert not is_prime(42), '42 - составное число'
    assert is_prime(73), '73 - простое число'


def test_type():
    with raises(TypeError):
        is_prime(3.14)


def test_value():
    """Проверяем только ошибку"""
    with raises(ValueError):
        is_prime(-100)


def test_value_with_text():
    """Проверяем и ошибку и текст, который она выдает"""
    with raises(ValueError, match=r'The number P must be greater than 1'):
        is_prime(1)


def test_warning_false(capfd):
    is_prime(100_000_001)
    captured = capfd.readouterr()
    assert captured.out == ('If the number P is prime, the check may take a long time.\n'
                            'Working...\n')


def test_warning_true(capfd):
    is_prime(100_000_007)
    captured = capfd.readouterr()
    assert captured.out == ('If the number P is prime, the check may take a long time.\n'
                            'Working...\n')


if __name__ == '__main__':
    main(['-v'])
