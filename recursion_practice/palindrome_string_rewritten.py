def is_palindrome_string(str):
    if len(str) > 1:
        if str[0] != str[-1]:
            return False
        else:
            return is_palindrome_string(str[1:-1])
    elif len(str) <= 1:
        return True


print(is_palindrome_string('abcddcba'))