from argparse import ArgumentParser

parser = ArgumentParser(description='My first argument parser', epilog='End helpinga')
# description - описание(название) нашего скрипта
# epilog - описание в конце вывода справки
parser.add_argument('numbers', metavar='N', type=float,
                    nargs='*',
                    help='press some numbers')
# numbers - имя списка, по которому можно к нему обращаться
# add_argument - добавляет аргументы после вызова в командной строке
# type - указывает на тип аргументов
# nargs = '*' - говорит, что все аргументы необходимо положить в список
# metavar='N' - для указания при вызове справки и тегом --help
# help='что ввести нужно' - указываем для демонстрации в справке

args = parser.parse_args()

print(f'В скрипт передано: {args}')

"""
что запускаем в командной строке:
python task_1.py 42 3.14 73
python task_1.py --help
python task_1.py -h
python task_1.py Hello World!
"""
