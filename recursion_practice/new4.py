def pick_k_in_array_get_max_sum(array, t, index, max_sum, n, k):
    if max_sum == None:
        max_sum = float('-inf')
    if index < n:
        if t == k - 1:
            max_sum = max(array[index], max_sum)
            return max_sum

        # 选择 array[index]
        select_sum = pick_k_in_array_get_max_sum(array, t + 1, index + 1, max_sum, n, k) + array[index]

        # 不选择 array[index]
        not_select_sum = pick_k_in_array_get_max_sum(array, t, index + 1, max_sum, n, k)

        return max(select_sum, not_select_sum)

    return 0

array = [1, 3, 2]
k = 3
n = len(array)
print(pick_k_in_array_get_max_sum(array, 0, 0, None, n, k))