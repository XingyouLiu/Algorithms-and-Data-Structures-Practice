def pick_k_in_array_get_max_sum(array, t, index, max_sum, sum_up, n, k):
    if max_sum == None:
        max_sum = float('-inf')
    if index < n:
        if t == k - 1:
            sum_up += array[index]
            max_sum = max(sum_up, max_sum)
            sum_up -= array[index]
            return max_sum

        # 选择 array[index]
        sum_up += array[index]
        max_sum = pick_k_in_array_get_max_sum(array, t + 1, index + 1, max_sum, sum_up, n, k)
        sum_up -= array[index]

        # 不选择 array[index]
        max_sum = pick_k_in_array_get_max_sum(array, t, index + 1, max_sum, sum_up, n, k)

    return max_sum

array = [1, 3, 2]
k = 3
n = len(array)
print(pick_k_in_array_get_max_sum(array, 0, 0, None, 0, n, k))