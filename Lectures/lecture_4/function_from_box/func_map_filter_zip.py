"""map(), filter(), zip()"""


def map_use(texts: list[str]):
    return map(lambda x: x.lower(), texts)


def filter_use(numbers: list[int]):
    """filter(function, iterable)"""
    return tuple(filter(lambda x: x > 0, numbers))


def zip_use(name: list[str], salaries: list[int], awards: list[float]) -> None:
    """zip(*iterable, strict=False)"""
    for name, salary, award in zip(name, salaries, awards):
        print(f'{name: >8} заработал {salary:.2f} денег и премию в {salary * award:.2f}')


my_texts = ["Привет", "ЗдоровА", "ПриветСТВую"]
my_numbers = [42, -73, 1024]

my_names = ['Иван', "Алексей", "Андрей"]
my_salaries = [125_000, 96_000, 109_000]
my_awards = [0.1, 0.25, 0.13, 0.99]

print(*map_use(my_texts))
print(filter_use(my_numbers))
zip_use(my_names, my_salaries, my_awards)
