def length_list(list):
    if list == []:
        return 0
    else:
        return 1 + length_list(list[1:])


print(length_list([1,3,5,7]))