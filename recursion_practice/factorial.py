def factorial(number):
    if number == 1:
        return number
    elif number == 2:
        return number * (number-1)
    else:
        return number * factorial(number-1)


print(factorial(4))

