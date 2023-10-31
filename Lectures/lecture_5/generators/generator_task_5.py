# Если на выходе нужен готовый список, оптимальным будет следующий код
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]

print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')

# А если нам не нужны все элементы разом. Например, мы в дальнейшем хотим
# перебирать значения по одному в цикле. В этом случае подойдет генераторное
# выражение без преобразования в список.


print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# генераторное выражение все элементы не хранит
for item in mult:
    print(f'{item = }')

# Важно! При написании кода заранее решите нужна вам сгенерированная
# коллекция целиком или нет. Не стоит тратить память на хранение всех
# элементов, если вы ими не пользуетесь одновременно.
