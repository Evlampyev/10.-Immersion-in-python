"""Работа с неизменяемыми типами данных"""

def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }')
    return a


a = 42
print(f"in main {a = }")
z = no_mutable(a)
print(f'{a = }\t{z = }')
