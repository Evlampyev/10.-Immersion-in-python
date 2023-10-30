import functools

f = open('mydata.bin', 'rb')
# чтение бинарного файла блоками фиксированного размера до тех пор, пока не будет достигнут конец файла
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()
