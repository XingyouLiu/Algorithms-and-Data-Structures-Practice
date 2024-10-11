def merge_sort(array):
    if len(array) <= 1:
        return array
    len_array = len(array)
    left = array[:len_array // 2]
    right = array[len_array // 2:]
    merged_array = merge_sort_help(merge_sort(left), merge_sort(right))
    return merged_array

def merge_sort_help(left, right, left_index = 0, right_index = 0, merged_array = None):
    if merged_array is None:
        merged_array = []

    if left_index >= len(left):
        merged_array.extend(right[right_index:])
        return merged_array
    elif right_index >= len(right):
        merged_array.extend(left[left_index:])
        return merged_array

    if left[left_index] < right[right_index]:
        merged_array.append(left[left_index])
        return merge_sort_help(left, right, left_index + 1, right_index, merged_array)
    else:
        merged_array.append(right[right_index])
        return merge_sort_help(left, right, left_index, right_index + 1, merged_array)


print(merge_sort([5,2,3,4,10,-3,80,-1]))

"""
归并排序的时间复杂度在最好、最坏和平均情况下都是O(n log n)，这使得它比如快速排序这样在最坏情况下为O(n^2)的算法更加稳定。
但是，归并排序需要额外的内存空间来存储临时数组，这是它的一个缺点。
尽管如此，它的稳定性和一致的性能使其在某些场景下非常有用，尤其是在那些数据集大小固定且空间不是主要限制因素的应用中。
"""