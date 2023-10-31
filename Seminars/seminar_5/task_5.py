# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

for num in range(1, 101):
    if num % 15 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Bizz"
    else:
        result = num
    print(result, end=" ")


print()
int_lst = [[i, 'Fizz', 'Buzz', 'FizzBuzz'][(i % 3 == 0) + (i % 5 == 0) * 2] for
           i in range(1, 101)]
print(*int_lst)
