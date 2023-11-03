import random
from sys import argv

print(random.uniform(int(argv[1]), int(
    argv[2])))  # случайное вещественное число от 10 до 1000
print(random.randrange(int(argv[1]), int(argv[2]),
                       int(argv[1])))  # случайное из range(10,1010,10)
print(random.sample(range(int(argv[1]), int(argv[2]),
                          int(argv[1])), 10)) # десять случайных чисел из range

# python3 task_4.py 10 1010
