def quick_sort(array):
    """
    此为总是选择数组第一个元素作为基准值的写法。
    也可以用其它选择基准值的方法（比如随机在数组中选择）
    """
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = [element for element in array if element < pivot]
    right = [element for element in array if element > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([2,1,8,3,7]))


"""
快速排序算法的效率取决于基准值的选择和分区操作。
在最佳情况下，每次分区都将列表均匀划分，这样可以达到最优的时间复杂度O(n log n);
然而，在最坏的情况下，如果每次分区操作总是选择最大或最小的元素作为基准值，那么算法的时间复杂度会退化到O(n^2)。

尽管在最坏情况下性能不佳，快速排序通常比其他O(n log n)算法，如归并排序或堆排序，在实际应用中表现得更好，原因是其内部循环可以在大多数架构上非常高效地实现。
"""