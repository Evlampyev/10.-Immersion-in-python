"""Enumerate, изменение порядка нумерации"""
animals = ['cat', 'dog', 'cow', 'wolf']
for i, animal in enumerate(animals, start=1):  # по умолчанию start=0
    print(f"{i} - {animal}")

data: int = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break
else:
    data += 5
print(data)
