# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
# и возвращает транспонированную матрицу.

def transpose(my_matrix: list[list]) -> list[list]:
    result = []
    count = 0
    for j in range(len(my_matrix[0])):
        temp_list = []
        for i in range(len(my_matrix)):
            temp_list.append(my_matrix[i][j])
        result.append(temp_list)
    return result


import warnings

warnings.filterwarnings('ignore')


# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки


# Введите ваше решение ниже

def transpose(matrix):
    result = []
    count = 0
    for j in range(len(matrix[0])):
        temp_list = []
        for i in range(len(matrix)):
            temp_list.append(matrix[i][j])
        result.append(temp_list)
    return result


print(transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))