# 希尔排序 Shell Sort
def shell_sort(array, gap = None):
    if gap is None:
        gap = len(array) // 2

    if gap == 1:
        return insertion_sort(array, gap)
    else:
        return shell_sort(insertion_sort(array, gap), gap // 2)


def insertion_sort(array, gap):
    for k in range(gap):
        for i in range(k, len(array), gap):
            min = array[i]
            min_index = i
            for j in range(i, len(array), gap):
                if array[j] < min:
                    min = array[j]
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]

    return array


print(shell_sort([6,1,0,2,7,10,-3,-5,-10]))


