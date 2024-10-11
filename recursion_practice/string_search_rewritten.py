def string_search(str, object):
    if str == '':
        return False
    elif str[0] == object:
        return True
    return string_search(str[1:], object)


print(string_search('Hello','o'))
