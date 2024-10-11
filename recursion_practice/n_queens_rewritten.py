def is_place_valid(chess_list, row_index, column_value):
    if row_index != 0:
        for i in range(row_index):
            if chess_list[i] == column_value:
                return False
            if row_index - i == column_value - chess_list[i] or row_index - i == chess_list[i] - column_value:
                return False
    return True


def n_queens_one_solution(n, row_index = None, solution = None):
    if solution == None:
        solution = [-1 for _ in range(n)]
    if row_index == None:
        row_index = 0

    if row_index == n:
        return solution

    for column_index in range(n):
        if is_place_valid(solution, row_index, column_index):
            solution[row_index] = column_index
            result = n_queens_one_solution(n, row_index = row_index + 1, solution = solution)
            if result is not None:
                return result
    solution[row_index] = -1

    return None


print(n_queens_one_solution(4))



def n_queens_all_solutions(n, row_index = None, solution = None, solutions_list = None):
    if solution == None:
        solution = [-1 for _ in range(n)]
    if solutions_list == None:
        solutions_list = []
    if row_index == None:
        row_index = 0

    if row_index == n:
        solutions_list.append(solution.copy())
        return

    for column_index in range(n):
        if is_place_valid(solution, row_index, column_index):
            solution[row_index] = column_index
            n_queens_all_solutions(n, row_index + 1, solution, solutions_list)
    solution[row_index] = -1

    if row_index == 0:
        return solutions_list


print(n_queens_all_solutions(6))

