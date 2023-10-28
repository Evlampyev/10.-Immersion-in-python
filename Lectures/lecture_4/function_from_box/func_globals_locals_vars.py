"""locals() и globals()"""

SIZE = 10


def func_locals(a, b, c):
    x = a + b
    print(f"{'From func_locals:': <17}\t{locals() = }")
    z = x + c
    return z


def func_globals(a, b, c):
    x = a + b
    print(f"{'From func_globals:': <17}\t{globals() = }")
    z = x + c
    return z


f = func_locals(1, 2, 3)

print(f"{'From main: ': <17}\t{globals() = }")
print(f'From main: {func_globals(1,2, 3) = }')

# изменяем словарь globals
x = 42
glob_dict = globals()
glob_dict['x'] = 73  # Переменная обязательно должна существовать
print(f'{x = }')

print(vars(int))
