def is_place_valid(chess_list, row_index, column_value):
    if row_index != 0:
        for i in range(row_index):
            if chess_list[i] == column_value:
                return False
            if row_index - i == column_value - chess_list[i] or row_index - i == chess_list[i] - column_value:
                return False
    return True

"""
获取n queens问题其中一个解的函数，递归和回溯过程分析：
假设我们在N Queens问题中的某一层递归，尝试在当前行的不同列放置皇后：
尝试放置皇后：在for j in range(n):循环中，我们尝试在当前行的每一列放置皇后。

递归调用：如果在某一列能够成功放置皇后（即is_place_valid返回True），我们进行递归调用，进入下一行。

栈帧压入：每次递归调用都会在调用栈上创建一个新的栈帧。

递归返回：如果在下一行（或更深层次的递归）中找不到合适的位置放置皇后，这次递归调用会返回None。

栈帧弹出：返回None意味着当前的栈帧被弹出，控制权回到了这次递归调用的上一层。


if result is not None: return result语句的作用分析：
在递归函数中，每当通过result = n_queens(n, row_index + 1, chess_list)进行递归调用时，函数会尝试在下一行放置皇后，并继续这个过程，直到达到以下两种情况之一：
1.找到解决方案：当row_index == n时，意味着已经成功在每一行放置了皇后，且没有冲突。此时，函数会返回当前的chess_list，这代表一个有效的解决方案。
2.无法放置皇后需要回溯：如果在当前行无法放置皇后而所有列都已经尝试过，函数会返回None，这表示需要在上一行尝试其他列。

执行 if result is not None: return result
当从递归调用返回时，以下两种情况会发生：
1.如果找到解决方案：
如果从更深层的递归调用返回了一个非None的解决方案（即一个有效的chess_list），那么if result is not None:条件成立，执行return result，将这个解决方案返回到上一层递归。
2.继续尝试当前行的其他列：
如果返回的是None，表示当前尝试失败，需要继续尝试当前行的其他列。此时，if result is not None:条件不成立，不会执行return result，而是继续当前递归层的循环。

当一层递归返回None到上一层：
当一层递归返回None到上一层时，上一层的执行流程在递归调用之后继续执行。在N Queens问题中，这意味着：
1.继续执行循环：
控制权回到了for j in range(n):循环的下一次迭代。这就是回溯过程的开始。我们尝试在当前行的下一列放置皇后。
2.如果所有列都尝试完：如果循环结束，所有列都已经尝试过并且都返回了None，则当前递归层次也返回None。这意味着需要继续回溯到更上一层的递归。
3.栈帧弹出：当前层次返回None后，其栈帧也被弹出，控制权回到了更上一层的递归调用。

总结
1.每个递归调用都对应于调用栈上的一个栈帧。
2.if result is not None: return result确保了一旦在递归的某一层找到一个有效的解决方案，这个解决方案就会被直接返回到最初的函数调用。
这个机制允许递归函数在找到有效解后立即中止更深层次的递归调用，并将解决方案传递回调用链的最顶端。
3.当一层递归无法找到解决方案并返回None时，其栈帧被弹出，控制权回到上一层递归。
 上一层递归继续执行循环的下一次迭代，尝试在当前行的下一列放置皇后，这实现了回溯。
 如果所有列都已尝试并返回None，则继续回溯到更上一层的递归。
"""
def n_queens_gpt_version(n, row_index=0, chess_list=None):
    if chess_list is None:
        chess_list = [-1 for _ in range(n)]  # 使用-1表示该行尚未放置皇后

    if row_index == n:
        return chess_list  # 找到一个解决方案

    for j in range(n):
        if is_place_valid(chess_list, row_index, j):
            chess_list[row_index] = j  # 放置皇后
            result = n_queens_gpt_version(n, row_index + 1, chess_list)
            if result is not None:
                return result
            chess_list[row_index] = -1

    # 当前行找不到合适位置，需要回溯到上一行
    return None



def n_queens_my_version(n, row_index=None, column_value=None, chess_list=None):
    if row_index == None:
        row_index = 0
    if column_value == None:
        column_value = 0
    if chess_list == None:
        chess_list = [-1 for i in range(n)]

    if row_index == n:
        return chess_list

    for j in range(column_value, n):
        if is_place_valid(chess_list, row_index, j):
            column_value = j
            chess_list[row_index] = column_value
            result = n_queens_my_version(n, row_index+1, 0, chess_list)
            if result != None:
                return result
            else:
                chess_list[row_index] = -1

    if row_index > 0:
        chess_list[row_index] = -1
        return n_queens_my_version(n, row_index-1, chess_list[row_index-1]+1, chess_list)

    return None



"""
获取n queens所有的可能解，为什么不需要if result == None、return None这类语句了？原因分析：

在原始的单解决方案版本中，if result is not None: return result是用来在找到一个解决方案时立即返回这个解决方案，并终止所有进一步的递归调用。
这是因为一旦找到了一个有效的解决方案，就没有必要继续尝试其他可能性了。

然而，在寻找所有解决方案的版本中，目的是探索棋盘的所有可能配置，即使在找到一个有效的解决方案后也需要继续探索。因此，逻辑发生了变化：
1. 收集解决方案：当找到一个解决方案时，我们将其添加到解决方案列表中，而不是立即返回。
2. 继续探索：即使找到了一个解决方案，我们仍然继续在当前行尝试放置皇后的下一列，以寻找其他可能的解决方案。

在这个新版本中，回溯是通过以下方式实现的：
1. 继续尝试当前行的其他列：当在某一列成功放置皇后后，我们递归调用自身以尝试在下一行放置皇后。
   如果这个递归调用不能找到解决方案（即无法在下一行放置皇后），我们会继续当前行的循环的下一次迭代，尝试在当前行的下一列放置皇后。这就实现了回溯的效果。
2. 回溯到上一行：当当前行的所有列都被尝试过后，函数自然地达到末尾并返回（没有显式的return语句）。这使得控制权回到上一层递归，继续尝试上一行的下一列。

结束递归的条件:
递归的终止条件在这里是当row_index等于棋盘的行数（即n）时，这意味着在每一行都成功放置了一个皇后。在这种情况下，我们找到了一个解决方案并将其添加到解决方案列表中。
"""
def n_queens_all_solutions(n, row_index=None, chess_list=None, solutions_list=None):
    if row_index == None:
        row_index = 0
    if chess_list == None:
        chess_list = [-1 for i in range(n)]
    if solutions_list == None:
        solutions_list = []

    if row_index == n:
        solutions_list.append(chess_list.copy())
        return

    for j in range(n):
        if is_place_valid(chess_list, row_index, j):
            chess_list[row_index] = j
            n_queens_all_solutions(n, row_index+1, chess_list, solutions_list)
            chess_list[row_index] = -1

    if row_index == 0:  #若执行到row_index == 0, 则意味着已经返回到了第一层递归，且第一行的所有列都已遍历尝试过，没有可能有其他解了！因此直接返回解列表。
        return solutions_list



print(n_queens_gpt_version(25))

print(n_queens_my_version(6))

print(n_queens_all_solutions(6))

