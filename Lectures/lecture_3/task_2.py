"""Строки"""

text = "Hello, world!"

print(text.replace('l', 'L'))  # что меняем, на что, сколько замен

print(text)
k = 123456789
print(f"{k = :_}")

text = '1 2 3 4 5'
res = text.split(' ')
print(res)


data = '/'.join(res)
print(data)

print(text.startswith('1 '))
print(text.startswith('2  3'))
print(text.endswith('5'))
print(text.endswith('4', 0, -2))

