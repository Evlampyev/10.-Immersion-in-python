"""Попадание из первого списка во второй"""

list1: list = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2: list = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
count: int = 0
for el in list1:
    if el in list2:
        count += 1
print(f"Количество совпадающих чисел: {count}")
