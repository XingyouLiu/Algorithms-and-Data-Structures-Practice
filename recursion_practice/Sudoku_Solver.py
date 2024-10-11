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
    if solutions == None:
        solutions = []

    is_filled = True
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                is_filled = False
                break
        if is_filled == False:
            break

    if is_filled:
        solutions.append([row[:] for row in sudoku])
        return

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1,10):
                    if is_valid(sudoku, i, j, num):
                        sudoku[i][j] = num
                        sudoku_solver(sudoku, solutions)
                        sudoku[i][j] = 0
                return solutions

    return solutions  #此句可以省略，但保留它可以使函数的行为更加明确。当其他人阅读您的代码时，他们可以立即看到这个函数最终返回的是解决方案列表。
    # 如果您的目标是编写清晰易懂的代码，那么即使这个return语句在逻辑上不是必需的，保留它也是有好处的，特别是在更复杂的函数中，明确函数的返回值有助于理解函数的行为。



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







