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


def sudoku_solver(sudoku, solutions_list = None):
    if solutions_list == None:
        solutions_list = []

    n = len(sudoku)
    for row_index in range(n):
        for column_index in range(n):
            if sudoku[row_index][column_index] == 0:
                for number in range(1, n + 1):
                    if is_valid(sudoku, row_index, column_index, number):
                        sudoku[row_index][column_index] = number
                        sudoku_solver(sudoku, solutions_list)
#在除了递归的第一层以外的其他层级运行以下两句，则意味着已在该空位处试尽1-9所有的数但没能找到合适的数，因此将该空位仍设为0并返回（回溯）到上一层；
#返回到第一层后运行以下两句，则意味着回溯到第一个空位处并已试尽1-9所有的数但没能找到合适的数，意味着已穷尽所有可能性但都没能找到新的解，因此跳出函数并返回解列表（解列表可能有解，也可能为空）
                sudoku[row_index][column_index] = 0
                return solutions_list

    solutions_list.append(sudoku.copy())
    #只有sudoku中不存在空位（即不存在0），即上一段落循环进行完毕且未进入if sudoku[row_index][column_index] == 0之后的语句（意味着未进入到下一层递归），才会执行此语句（将已无空位的sudoku添加进解列表中）

    #return solutions_list（这里的此语句可有可无）



def sudoku_solver_1(sudoku, solutions_list = None, row_index = None, column_index = None):
    if solutions_list == None:
        solutions_list = []
    if row_index == None:
        row_index = 0
    if column_index == None:
        column_index = 0

    if row_index == 9:
        solutions_list.append([row[:] for row in sudoku])
        return
    if column_index == 9:
        sudoku_solver_1(sudoku, solutions_list, row_index + 1, 0)
        return

    if sudoku[row_index][column_index] == 0:
        for number in range(1, 10):
            if is_valid(sudoku, row_index, column_index, number):
                sudoku[row_index][column_index] = number
                sudoku_solver_1(sudoku, solutions_list, row_index, column_index + 1)
                sudoku[row_index][column_index] = 0
    else:
        sudoku_solver_1(sudoku, solutions_list, row_index, column_index + 1)

    if row_index == 0 and column_index == 0:
        return solutions_list


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

print(sudoku_solver_1(sudoku))

print(sudoku_solver(sudoku))




