def full_permutation(array, permutated_part = None, current_permutations_1 = None, current_permutations_2 = None, permutations_list = None):
    if permutated_part == None:
        permutated_part = [array[-1]]
    if current_permutations_1 == None:
        current_permutations_1 = []
    if current_permutations_2 == None:
        current_permutations_2 = []
    if permutations_list == None:
        permutations_list = []
    len_array = len(array)
    len_permutated_part = len(permutated_part)
    if len_permutated_part == len_array:
        permutations_list = current_permutations_1
        return len(permutations_list), permutations_list
    if len_permutated_part == 1:
        current_permutations_1.append(permutated_part)
    former_element = array[:(len_array - len_permutated_part)][-1]
    for i in range(len_permutated_part + 1):
        for item in current_permutations_1:
            item_copy = item.copy()
            item_copy.insert(i, former_element)
            one_permutation = item_copy
            current_permutations_2.append(one_permutation)
    permutated_part.insert(0, former_element)
    return full_permutation(array, permutated_part=permutated_part, current_permutations_1=current_permutations_2)


print(full_permutation([2,5,1,3]))


def full_permutation_backtrack(numbers, start = None, permutations_list = None):
    if start == None:
        start = 0
    if permutations_list == None:
        permutations_list = []

    if start == len(numbers):
        permutations_list.append(numbers.copy())

    for i in range(start, len(numbers)):
        numbers[start], numbers[i] = numbers[i], numbers[start]
        full_permutation_backtrack(numbers, start + 1, permutations_list)
        numbers[start], numbers[i] = numbers[i], numbers[start]

    return permutations_list

print(full_permutation_backtrack([2,5,1]))

"""
array = [2,5,1]
1:
start = 0
for i in range(0, 3):
i=0, numbers[0]-nunbers[0], numbers = [2,5,1]
1-1:
start = 1
for i in range(1, 3):
i=1, numbers[1]-numbers[1], numbers = [2,5,1]
1-1-1:
start = 2
for i in range(2, 3):
i=2, numbers[2]-numbers[2], numbers = [2,5,1]
1-1-1-1:
start = 3
permutations_list = [[2,5,1]]
for i in range(3, 3): return to 1-1-1 and continue
1-1-1:
numbers[2]-numbers[2], numbers = [2,5,1]
return to 1-1 and continue
1-1:
numbers[1]-numbers[1], numbers = [2,5,1]
for i in range(1, 3):
i=2, numbers[2]-numbers[1], numbers = [2,1,5]
1-1-2:
start = 2
for i in range(2, 3):
i = 2, numbers[2]-numbers[2], numbers = [2,1,5]
1-1-2-1:
start = 3
permutations_list = [[2,5,1], [2,1,5]]
for i in range(3, 3): return to 1-1-2 and continue
1-1-2:
numbers = [2,1,5]
return to 1-1 and continue
1-1:
numbers[2]-numbers[1], numbers = [2,5,1]
return to 1 and continue
1:
for i in range(0, 3):
i=1, numbers[1]-nunbers[0], numbers = [5,2,1]
............
"""
