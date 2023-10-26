"""Словари продолжение"""

my_dict = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'ten': 10,
           }

print(my_dict.setdefault('ten',
                         555))  # если нет в словаре, то выводит 555, если есть, то вывод на экран значения по ключу
print(my_dict.values())  # все значения в словаре
print(my_dict.pop('one'))  # ключ будет удален из словаря, а его значение будет выведено на экран

my_dict['one'] = my_dict['four']
print(my_dict)
