def max_sub_array_sum(array):
    current_max = array[0]
    global_max = array[0]
    if len(array) <= 1:
        return global_max
    for i in range(1, len(array)):
        if current_max < array[i] and array[i-1] < 0:
            current_max = array[i]
        elif array[i] + current_max > current_max and array[i-1] >= 0:
            current_max += array[i]
        if current_max > global_max:
            global_max = current_max
    return global_max


def max_sub_array_sum_simplified_version(array):
    current_max = global_max = array[0]
    for num in array[1:]:
        current_max = max(num, current_max + num)
        global_max = max(current_max, global_max)
    return global_max


print(max_sub_array_sum([1,2,3,4,5,-3,-30,100,-1000,200,1,-1]))
print(max_sub_array_sum_simplified_version([1,2,3,4,5,-3,-30,100,-1000,200,1,-1]))



