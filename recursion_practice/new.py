def pick_k_in_array_get_max_sum(array, t, index, max_sum, sum_up, n, k):
    if max_sum == None:
        max_sum = float('-inf')
    if t == k - 1:
        max_sum = max(sum_up, max_sum)
        return max_sum
    if index < n:
        sum_up += array[index]
        max_sum = pick_k_in_array_get_max_sum(array, t + 1, index + 1, max_sum, sum_up, n, k)
        sum_up -= array[index]
        max_sum = pick_k_in_array_get_max_sum(array, t, index + 1, max_sum, sum_up, n, k)

    return max_sum

array = [93,463,179,2488,619,2006,1561,137,53,1765,2304,1459,1768,450,1938,2054,466,331,670,1830,1550,1534,2164,1280,2277,2312,1509,867,2223,1482,2379,1032,359,1746,966,232,67,1203,2474,944,1740,1775,1799,1156,1982,1416,511,1167,1334,2344]
k = 42
n = len(array)
print(pick_k_in_array_get_max_sum(array, 0, 0, None, 0, n, k))