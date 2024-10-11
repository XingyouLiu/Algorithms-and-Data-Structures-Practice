def bubble_sort(array):
    if len(array) <= 1:
        return array

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

    return bubble_sort(array[:-1]) + [array[-1]]


print(bubble_sort([5,2,1,0,3]))