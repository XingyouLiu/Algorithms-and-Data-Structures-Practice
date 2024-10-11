def search_list_item(list, item, index=0):
    if list == []:
        return False
    elif list[0] == item:
        return True, index
    else:
        index += 1
        return search_list_item(list[1:], item, index)


print(search_list_item([1,2,3,4,5], 5))