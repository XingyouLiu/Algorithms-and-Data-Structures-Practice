# 二分法查找 binary search：
def binary_search(my_list, item):
    length = len(my_list)
    left = 0
    right = length
    is_founded = False
    while is_founded == False:
        mid = left + (right - left) // 2
        if my_list[mid] == item:
            is_founded = True
            return mid
        elif my_list[mid] < item:
            left = mid + 1
        else:
            right = mid
        if left >= right:
            break
    return 'None'


print(binary_search([1, 2, 4, 3, 5, 6, 7], 100))


# 二分法查找 递归写法：

def binary_search_senior(my_list, item, offset):
    # 设置一个参数offset（偏移量），用于记录每次left改变后的新list，与最初left之间的偏移量。这样，只要用偏移量加上新list中所寻元素的索引，即可得到所寻元素在原list中的索引。
    left = 0
    right = len(my_list)
    mid = left + (right - left) // 2
    if left >= right:
        return '数组中没有你要查找的元素！'
    if my_list[mid] < item:
        left = mid + 1
        offset = offset + mid + 1
    elif my_list[mid] > item:
        right = mid
    elif my_list[mid] == item:
        return mid + offset
    return binary_search_senior(my_list[left:right], item, offset)


print(f'该元素的索引是：{binary_search_senior(my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], item=13, offset=0)}')