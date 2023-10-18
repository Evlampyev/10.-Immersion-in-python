"""Ряды у елки"""
rows = int(input("Сколько рядов у елки: "))
maximum = 2 * rows + 1
for i in range(rows):
    count = 2 * i + 1
    print(" " * ((maximum - count) // 2) + "*" * count)

print("Вторая елка")

for i in range(rows):
    print(f'{"*" * (2 * i + 1):/^{2 * rows + 1}}')
