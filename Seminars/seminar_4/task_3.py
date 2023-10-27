# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def make_new_dict(data: str) -> dict[str, int]:
    left, right = sorted(map(int, data.split()))
    unicode = {}
    for i in range(left, right + 1):
        unicode[chr(i)] = i
    return unicode

def get_unicode_dict(id_pair: str) -> dict[str, int]:
    id_1, id_2 = sorted(map(int, id_pair.split()))
    return {chr(cur_id): cur_id for cur_id in range(id_1, id_2 + 1)}


print(make_new_dict('1000 900'))
print(get_unicode_dict('900 1000'))
