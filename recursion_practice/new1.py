def generate_combinations(array, index, k, current_combination, all_combinations):
    if len(current_combination) == k:
        all_combinations.append(current_combination[:])
        return

    if index >= len(array):
        return

    # 选择 array[index]
    current_combination.append(array[index])
    generate_combinations(array, index + 1, k, current_combination, all_combinations)
    current_combination.pop()

    # 不选择 array[index]
    generate_combinations(array, index + 1, k, current_combination, all_combinations)

def pick_k_in_array_get_max_sum(array, k):
    all_combinations = []
    generate_combinations(array, 0, k - 1, [], all_combinations)

    max_sum = float('-inf')
    for combination in all_combinations:
        max_sum = max(max_sum, sum(combination))

    return max_sum

array = [1, 3, 2]
k = 3
print(pick_k_in_array_get_max_sum(array, k))