from sys import argv

print('start')
print(argv)
print('stop')

#  после запуска в терминале ОС строки:
# python task_2.py -d 42 -s "Hello world!" -k 100

# получим следующий список:
# ['script.py', '-d', '42', '-s', 'Hello world!', '-k', '100']
# в [0] - всегда имя файла, потом все остальные аргументы,
# с которыми можно работать
