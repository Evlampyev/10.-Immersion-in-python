def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result


# Значение после yield возвращается из функции. Сама функция запоминает своё
# состояние: строку, на которой остановилось выполнение, значения локальных
# переменных. Повторный вызов функции продолжает работу с момента остановки.


def gen(n):
    number = 1
    for j in range(1, n + 1):
        number *= j
    yield number

# Теперь внутри функции не создаётся пустой список для результатов. В цикле
# вычисляется факториал очередного числа. Далее команда yield возвращает
# значение. Следующий вызов вернёт функцию к циклу for для вычисления
# очередного числа.




for i, num in enumerate(factorial(11), start=1):
    print(f"{i}! = {num}")

for i, num in enumerate(factorial(10), start=1):
    print(f"{i: >2}! = {num:.>8}")
