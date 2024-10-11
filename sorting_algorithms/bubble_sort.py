# 冒泡排序 bubble sort
def bubble_sort(my_list):
    for i in range(0, len(my_list) - 1):
        swapped = False
        # a=0
        for j in range(0, len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                # a=my_list[j]
                # my_list[j]=my_list[j+1]
                # my_list[j+1]=a
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]  # python交换两个变量值的简易做法
                swapped = True
            else:
                continue

        if swapped == False:
            break
    return my_list


print(bubble_sort([10, 3, -2, -0.5, 3.23]))


####递归实现冒泡排序，在return处的操作需要留意！！！！！
def bubble_sort_senior(my_list):
    if len(my_list) == 1:
        return my_list
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    return bubble_sort_senior(my_list[:-1]) + [my_list[-1]]


print(bubble_sort_senior([10, 3, -2, -0.5, 3.23]))