import numpy
from random import randint


class Matrix:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.data = numpy.zeros((rows, columns), dtype=int)

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        """
        Задача 3. Создайте класс Матрица.
        Добавьте методы для: - вывода на печать,
            - сравнения,
            - сложения,
            - *умножения матриц
        """
        return f"Matrix({self.rows}, {self.columns})"

    def __eq__(self, other: 'Matrix') -> bool:
        if isinstance(other, Matrix):
            return numpy.array_equal(self.data, other.data)
        return False

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
            result_matrix = Matrix(self.rows, self.columns)
            result_matrix.data = self.data + other.data
            return result_matrix
        else:
            raise ValueError(
                "Матрицы должны иметь одинаковый размер для сложения")

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if isinstance(other, Matrix) and self.columns == other.rows:
            result_matrix = Matrix(self.rows, other.columns)
            result_matrix.data = numpy.dot(self.data, other.data)
            return result_matrix
        else:
            raise ValueError(
                "Число столбцов первой матрицы должно быть равно числу строк второй матрицы для умножения")


if __name__ == '__main__':
    matrix1 = Matrix(2, 2)
    matrix1.data = numpy.array([[randint(1, 100), randint(1, 100)], [
                               randint(1, 100), randint(1, 100)]])

    matrix2 = Matrix(2, 2)
    matrix2.data = numpy.array([[randint(1, 100), randint(1, 100)], [
                               randint(1, 100), randint(1, 100)]])

    print(f'Матрица 1: \n {matrix1}')
    print(f'Матрица 2: \n {matrix2}')

    if matrix1 == matrix2:
        print("Матрицы равны")
    else:
        print("Матрицы не равны")

    try:
        result_matrix = matrix1 + matrix2
        print(f'Сумма матриц: \n {result_matrix}')
    except ValueError as e:
        print(e)

    try:
        product_matrix = matrix1 * matrix2
        print(f'Произведение матриц: \n {product_matrix}')
    except ValueError as e:
        print(e)
