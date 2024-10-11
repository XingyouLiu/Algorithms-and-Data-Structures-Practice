def reverse_string(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + reverse_string(str[:-1])

print(reverse_string('abcde'))