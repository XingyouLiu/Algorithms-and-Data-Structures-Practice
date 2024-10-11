import random
import time

test_list = []
# for i in range(500):
test_list.extend([9, 8, 7, 6, 5])

#快速排序 quick sort：
def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[0]
    less_list = []
    larger_list = []
    for number in my_list[1:]:
        if number < pivot:
            less_list.append(number)
        else:
            larger_list.append(number)
    return quick_sort(less_list) + [pivot] + quick_sort(larger_list)


start_time1 = time.time()
print(quick_sort(test_list))
end_time1 = time.time()
print(end_time1 - start_time1)


# 随机在数组中选择基准值的快速排序：
def senior_quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot_index = random.randint(0, len(my_list) - 1)
    pivot = my_list[pivot_index]
    less_list = []
    larger_list = []
    i = 0
    for number in my_list:
        if i == pivot_index:
            i += 1
            continue
        elif number < pivot:
            less_list.append(number)
            i += 1
        else:
            larger_list.append(number)
            i += 1
    return senior_quick_sort(less_list) + [pivot] + senior_quick_sort(larger_list)


start_time2 = time.time()
print(senior_quick_sort(test_list))
end_time2 = time.time()
print(end_time2 - start_time2)