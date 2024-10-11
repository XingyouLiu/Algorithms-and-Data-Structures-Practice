def insertion_sort(array, sorted_part = None):
    if sorted_part is None:
        sorted_part = [array[0]]

    if len(array) == len(sorted_part):
        return sorted_part

    un_sorted_part = [element for element in array if element not in sorted_part]
    current = un_sorted_part.pop(0)
    sorted_part = insertion_sort_help(sorted_part, current)
    return insertion_sort(array, sorted_part)


def insertion_sort_help(sorted_part, current, index = 0):
    if index >= len(sorted_part):
        sorted_part.append(current)
        return sorted_part
    if sorted_part[index] < current:
        return insertion_sort_help(sorted_part, current, index + 1)
    elif sorted_part[index] > current:
        sorted_part = sorted_part[:index] + [current] + sorted_part[index:]
        return sorted_part


print(insertion_sort([3,7,1,0,4,-2,-7,90]))

print(insertion_sort([1]))


def insertion_sort_loop(array):
    for i in range(0, len(array)):
        min = array[i]
        min_index = i
        for j in range(i, len(array)):
            if array[j] < min:
                min = array[j]
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array

print(insertion_sort_loop([3,7,1,0,4,-2,-7,90]))