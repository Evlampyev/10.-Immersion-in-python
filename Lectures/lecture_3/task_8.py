"""Тип байты"""

text_en = 'Hello, worlf!'
res = text_en.encode('utf-8')
print(res, type(res))

text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))

x = bytes(b'\xd0\x9f')  # не изменяемый тип
x = bytearray(b'\xd0\x9f')  # изменяемый тип

print(f"{x = }")
