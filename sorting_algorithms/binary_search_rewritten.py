def binary_search(array, item):
    if array == []:
        return False
    elif array[0] == item:
        return True

    mid_index = len(array) // 2
    if array[mid_index] == item:
        return True
    elif array[mid_index] > item:
        return binary_search(array[:mid_index], item)
    else:
        return binary_search(array[mid_index + 1:], item)


print(binary_search([1,3,5,7,9], -1))