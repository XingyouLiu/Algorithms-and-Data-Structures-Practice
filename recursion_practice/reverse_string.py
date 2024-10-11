def reverse_string(str):
    if len(str) <= 1:
        reversed = str
    else:
        reversed = reverse_string(str[1:]) + str[0]
    return reversed


print(reverse_string('haoren'))