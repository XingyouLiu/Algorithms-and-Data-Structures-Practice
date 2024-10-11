# 插入排序 insertion sort  循环版：
def insertion_sort_loop(array):
    array_1 = [array[0]]
    for i in range(1, len(array)):
        if len(array_1) == 1:
            if array_1[0] <= array[i]:
                array_1.insert(1, array[i])
            else:
                array_1.insert(0, array[i])
        else:
            for k in range(0, len(array_1)):
                if array[i] <= array_1[0]:
                    array_1.insert(0, array[i])
                    break
                elif array[i] > array_1[len(array_1) - 1]:
                    array_1.append(array[i])
                    break
                elif array[i] > array_1[k] and array_1[k + 1] >= array[i]:
                    array_1.insert(k + 1, array[i])
                    break
    return array_1


print(insertion_sort_loop([1, 5, 2, 7, 3, 10]))


# 插入排序  insertion sort  （递归，错误版，需要继续研究）
def insertion_sort(my_list):
    if len(my_list) == 1:
        return my_list
    if len(my_list) == 2:
        if my_list[0] > my_list[1]:
            my_list[0], my_list[1] = my_list[1], my_list[0]
        return my_list
    for i in range(1, len(my_list)):
        my_list = insertion_sort(my_list[:i + 1]) + my_list[i + 1:]
    return my_list


print(insertion_sort([5, 2, 3, 1]))