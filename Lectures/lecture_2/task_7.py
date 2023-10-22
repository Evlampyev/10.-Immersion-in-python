"""Работа со строками"""
data: str = input("Ваш текст: ")
if data.isdecimal():
    num: int = int(data)
    num_bin = bin(num)
    num_oct = oct(num)
    num_hex = hex(num)
    print(num, num_bin, num_oct, num_hex)
else:
    print(f"Текст в ASCII: {data.isascii()}")
