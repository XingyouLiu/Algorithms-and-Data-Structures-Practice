def is_valid(sudoku, row_index, column_index, number):
    for num in sudoku[row_index]:
        if num == number:
            return False
    for num in [row[column_index] for row in sudoku]:
        if num == number:
            return False
    start_row, start_col = row_index // 3 * 3, column_index // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == number:
                return False
    return True

def sudoku_solver(sudoku, solutions=None):
    if solutions is None:
        solutions = []

    # 查找第一个空单元格
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(sudoku, i, j, num):
                        sudoku[i][j] = num
                        sudoku_solver(sudoku, solutions)
                        sudoku[i][j] = 0  # 回溯
                return solutions  # 一旦尝试了所有数字或需要回溯，就返回解决方案

    # 如果没有空单元格，则添加解决方案
    solutions.append([row[:] for row in sudoku])
    return solutions #本句也可以省略


sudoku = [
    [2, 9, 5, 7, 4, 3, 8, 6, 1],
    [4, 3, 1, 8, 6, 5, 9, 0, 0],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 2, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [1, 5, 4, 9, 3, 8, 6, 0, 0]
]

print(sudoku_solver(sudoku))

