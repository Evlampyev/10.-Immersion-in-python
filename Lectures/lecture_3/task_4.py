"""Словарь"""
TEN = 'ten'
a = {
    'one': 42,
    'two': 3.14,
    'ten': 'Hello'
}
b = dict(one=42, two=3.14, ten='Hello')

c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello')])

print(a == b == c)

# Три идентичных словаря, заданных различными способами

print(c)
x = 5
c['five'] = x  # добавление элемента в словарь,
                # указываем ключ присваиваем значение
print(c)

print(c[TEN])
print(c.get('two'))
print(c.get('six'))  # такого ключа нет -> None
print(c.get('six', 5)) #  5 - значение по умолчанию, выводится если нет такого ключа
                        # такого ключа нет -> 5
print(c.get('ten', 5))  # такой ключ есть, поэтому значение по ключу,
                        # значение по умолчанию игнорится
