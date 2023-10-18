"""Проверить год на високосность"""
year: int = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    result: str = f"Год {year} является високосным"
else:
    result = f"Год {year} не високосный"

print(f"Первая часть - {result}")

if year % 4 == 0:
    if year % 100 != 0:
        result: str = f"Год {year} не високосный"
    else:
        result = f"Год {year} год является високосным"
elif year % 400 == 0:
    result: str = f"Год {year} является високосным"
else:
    result = f"Год {year} не високосный"

print(f"Во втором случае - {result}")


if year % 4 == 0:
    if year % 100 != 0:
        result = f"Год {year} является высокосным"
    else:
        result = f"Год {year} не высокосный"
elif year % 400 == 0:
    result = f"Год {year} является высокосным"
else:
    result = f"Год {year} НЕ является высокосным"


print(result)