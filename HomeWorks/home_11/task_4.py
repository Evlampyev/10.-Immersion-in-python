class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = []
        for _ in range(rows):
            self.data.append([0] * cols)

    def __str__(self):
        result = ''
        for row in self.data:
            for col in row:
                result += str(col) + ' '
            result += '\n'
        return result[:-2]

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.cols == other.cols and self.rows == othe:
                res = Matrix(self.rows, other.cols)
                for i in range(self.rows):
                    for j in range(self.cols):
                        res.data[i][j] = self.data[i][j] + other.data[i][j]
                return res
            else:
                raise SyntaxError("Матрицы не совместимы")
        else:
            raise TypeError("Второй объект не матрица")

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.data[i][j] != other.data[i][j]:
                            return f'Матрицы не равны'
                return f'Матрицы равны'
            else:
                return f'Матрицы не равны'
        else:
            raise TypeError("Второй объект не матрица")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols ==other
        else:
            raise TypeError("Второй объект не матрица")


if __name__ == '__main__':
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    #  Выводим матрицы
    print(matrix1)

    print(matrix2)
    print(matrix2 == matrix1)
    print(matrix1 + matrix2)
