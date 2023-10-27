# Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def print_text(text: str):
    unicode = []
    for ch in set(text):
        unicode.append(ord(ch))
    return sorted(unicode, reverse=True)


def sorted_unique_symbols(text: str) -> list[int]:
    return list(sorted(map(ord, set(text)), reverse=True))


data = 'Напишите функцию, которая принимает строку текста.'
print(print_text(data))
print(sorted_unique_symbols(data))
