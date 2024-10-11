def string_search(str, value, index=0):
    """
        基线条件（Base Case）：基线条件告诉递归何时停止。
        在这个函数中，基线条件是当字符串 str 为空时（str == ''），表示我们已经检查完整个字符串，没有找到要查找的值 value。在这种情况下，函数返回 False，表示未找到。

        递归条件（Recursive Case）：递归条件描述了递归函数在没有达到基线条件时执行的部分。
        在这个函数中，递归条件是比较字符串的第一个字符 str[0] 是否等于要查找的值 value。
        如果它们相等，函数返回当前的 index，表示找到了 value。如果它们不相等，函数将问题缩小为比较去掉第一个字符的子字符串，并递归调用 string_search 函数.
    """
    if str == '':
        return False
    elif str[0] == value:
        return index
    else:
        return string_search(str[1:], value, index + 1)


print(string_search('12345', '5'))