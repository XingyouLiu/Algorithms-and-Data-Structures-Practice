def pick_k_in_array_get_max_sum(array, index, k):
    if k == 0:
        return 0

    if index >= len(array):
        return float('-inf')

    # 选择 array[index]
    select_sum = array[index] + pick_k_in_array_get_max_sum(array, index + 1, k - 1)

    # 不选择 array[index]
    not_select_sum = pick_k_in_array_get_max_sum(array, index + 1, k)

    return max(select_sum, not_select_sum)

array = [1, 3, 2]
k = 2
print(pick_k_in_array_get_max_sum(array, 0, k))