"""
Сложность  O(n^2), так как функция имеет вложенный цикл, который зависит от длины матрицы
Функция принимает матрицу со сторонами m*n, где будет искать квадраты подматриц и будет их считать .
Функция возвращает колличество квадратов матриц.
"""

def countSquares(matrix):
    count = matrix.count(1)
    count = 0
    for i in range(len(matrix)):       # Цикл проходит по длине матрице
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:      # Проверяет, будут ли элементы матрицы равны 1
                count += 1             # Если элементы матрицы = 1, то идет прибавление 1
            if i == 0 or j == 0:
                continue               # Если одно из значений циклов равно 0 то цикл продолжается
            e_val = matrix[i][j]
            matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1],matrix[i-1][j]) + 1 if matrix[i][j] == 1 else 0
            count = count + matrix[i][j] - e_val
    return count

print(countSquares([[1, 0, 1], [1, 0, 0], [1, 1, 1]]))
