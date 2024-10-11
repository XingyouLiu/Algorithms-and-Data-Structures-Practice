def fabonacci_nth_item(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1 + 2
    else:
        return n + fabonacci_nth_item(n-1)

print(fabonacci_nth_item(8))