"""чтение методом readline"""

with open('../text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res,
              end="")  # end - для исключения двойного перехода на новую строку
 # При чтении readline возвращает строку с символом переноса на конце

SIZE = 100
with open('../text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)

# Передача положительного числа в качестве аргумента задаёт границу для длины
# строки. Если строка короче границы, она возвращается целиком. А если больше, то
# возвращается часть строки заданного размера. При этом следующий вызов метода
# вернёт продолжение строки снова фиксированного размера или остаток до конца,
# если она короче.
