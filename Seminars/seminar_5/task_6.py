# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

temp = '\n'
lst_1 = [f'{j: >2} * {i: >2} = {i * j: >2} {temp * (j // 5)}' for i in
         range(2, 11) for j in range(2, 6)]
print(*lst_1)

print('\n\n'.join(['\n'.join(
    ['\t\t'.join([f'{y} x {x} = {x * y:>2}' for y in range(2 + k, 6 + k)]) for x
     in range(2, 10)]) for k in [0, 4]]))
