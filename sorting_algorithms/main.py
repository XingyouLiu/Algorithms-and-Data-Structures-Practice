import time
import random


"""递归写法练习 递归写法练习 递归写法练习 递归写法练习 递归写法练习 递归写法练习 递归写法练习 递归写法练习 递归写法练习 递归写法练习 """
# sum(list)

def Sum(my_list):
    if my_list == []:
        return 0
    return my_list[0] + Sum(my_list[1:])


print(Sum([2, 4, 6]))


# lenth(list)
def Count(my_list):
    if my_list == []:
        return 0
    return 1 + Count(my_list[1:])


print(Count([2, 4, 6, 8, 10]))


# max(list)
def Max(my_list):
    if len(my_list) == 2:
        if my_list[0] > my_list[1]:
            return my_list[0]
        else:
            return my_list[1]
    if my_list[0] > Max(my_list[1:]):
        return my_list[0]
    else:
        return Max(my_list[1:])


print(Max([-8, -9, -1, -10, -100, -32, -98]))