"""Таблица умножения как в детской тетради через f строку"""
step: int = 4
part_begin: int = 2
part_end: int = 6
flag: int = 0
while flag < 2:
    for i in range(2, 11):
        for j in range(part_begin, part_end):
            print(f"{j:>2} x {i:>2} = {i * j:>2}" + ' ' * step, end="")
        print()
    print()
    flag += 1
    part_begin += step
    part_end += step
