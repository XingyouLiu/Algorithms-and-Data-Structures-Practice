def selection_sort(array, start = 1):
    if start >= len(array):
        return array

    min = array[start - 1]
    min_index = start - 1
    for i in range(start, len(array)):
        if min > array[i]:
            min = array[i]
            min_index = i
    array[start - 1], array[min_index] = array[min_index], array[start - 1]
    return selection_sort(array, start + 1)


print(selection_sort([3,7,1,9,0,-10,99]))