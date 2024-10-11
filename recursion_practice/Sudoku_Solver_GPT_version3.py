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

def sudoku_solver(sudoku, row=None, col=None, solutions=None):
    if solutions == None:
        solutions = []
    if row == None:
        row = 0
    if col == None:
        col = 0

    if row == 9:
        solutions.append([row[:] for row in sudoku])  # 返回数独的一个副本作为解决方案
        return
    if col == 9:
        sudoku_solver(sudoku, row + 1, 0, solutions)  # 移到下一行
        return

    if sudoku[row][col] == 0:
        for num in range(1, 10):
            if is_valid(sudoku, row, col, num):
                sudoku[row][col] = num
                sudoku_solver(sudoku, row, col + 1, solutions)
                sudoku[row][col] = 0  # 回溯
    else:
        sudoku_solver(sudoku, row, col + 1, solutions)
        #return solutions
    if row == 0  and col == 0:
        return solutions

    #return sudoku_solver(sudoku, row, col + 1, solutions)




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