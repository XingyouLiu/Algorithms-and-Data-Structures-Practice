"""
堆通常使用列表来表示。堆的列表表示与二叉搜索树的表示方式不同，因为堆是一个完全二叉树，可以使用列表来紧凑地表示节点的关系。
以下是一个示例用列表表示的最大堆：
[10, 9, 8, 7, 6, 4]
列表的第一个元素（索引0）是根节点，然后依次是其左子节点、右子节点，再到下一层的左子节点、右子节点，以此类推。
这种表示方式使得堆的操作更容易实现，因为您可以根据元素的索引计算出其父节点和子节点的索引。

堆是一个完全二叉树，不需要像二叉搜索树那样使用左指针和右指针来表示节点之间的关系。
在堆的列表表示中，您可以使用索引来计算节点的父节点、左子节点和右子节点，这使得堆的操作更加高效。
因为堆具有特定的结构，您可以根据索引计算出与节点相关的其他节点，而不需要额外的指针。

对于一个节点在索引 i 处，其父节点的索引是 (i-1)//2，左子节点的索引是 2*i+1，右子节点的索引是 2*i+2。
这种索引计算方式使得在堆中进行上浮和下沉等操作变得更加高效，因为您可以直接访问元素的索引，而不需要沿着指针遍历树。
"""

class Heap():
    def __init__(self, heap_type='max'): #定义堆类型为最大堆
        self.heap_list = []
        self.heap_type = heap_type

    def is_empty(self):
        return len(self.heap_list) == 0

    def wrong_insert(self, value, list_left=None, list_right=None):
        """
        此方法的错误原因是：其目的为将堆列表中的元素从大到小排序，这样输出的也满足最大堆的性质，但是最大堆并不要求所有元素从大到小排序，只要求母节点大于子节点！
        即，所有元素由大到小排序，是最大堆的充分不必要条件。
        """
        if self.is_empty():
            self.heap_list = [value]
        else:
            if list_left == None:
                list_left = []
            if list_right == None:
                list_right = self.heap_list
            if list_right == []:
                list_right = [value]
                self.heap_list = list_left + list_right
            elif value > list_right[0]:
                list_right = [value] + list_right
                self.heap_list = list_left + list_right
            else:
                self.wrong_insert(value, list_left=list_left + [list_right[0]], list_right=list_right[1:])


    def insert(self, value):
        """
        此方法为正确方法，先将新值插入原堆的末尾，然后利用子节点和母节点索引关系的公式，使新值与其母节点比较。
        若新值小于母节点值，则无需任何操作；若新值大于母节点值，则将二者交换位置。此为“上浮”。
        """
        self.heap_list.append(value)
        self.heapify_up(index = len(self.heap_list)-1)

    def heapify_up(self, index):
        if index != 0:
            parent_index = (index-1) // 2
            if self.heap_list[parent_index] < self.heap_list[index]:
                self.heap_list[parent_index], self.heap_list[index] = self.heap_list[index], self.heap_list[parent_index]
                self.heapify_up(parent_index)


    def delete_root(self):
        """
        1. 首先，将根节点的值保存在一个临时变量中，以便稍后返回。
        2. 将根节点的值替换为堆的最后一个元素（即堆中的最后一个元素）的值。
        3. 删除堆的最后一个元素。
        """
        if self.is_empty():
            return None
        elif len(self.heap_list) == 1:
            return self.heap_list.pop()
        else:
            original_root = self.heap_list[0]
            self.heap_list[0] = self.heap_list[-1]
            self.heap_list.pop()
            self.sink(index = 0, list=self.heap_list)
            return original_root

    def sink(self, index, list):
        """
        4. 开始下沉操作，从根节点开始向下比较根节点和其子节点的值，以找到较大的子节点。
        5. 如果根节点的值小于其中一个子节点的值，交换根节点与该子节点的值，以确保根节点的值大于等于其子节点的值。
        6. 重复步骤4和5，直到根节点的值大于等于其子节点的值，或者直到达到堆的底部（没有更多的子节点可以比较）。
        """
        if index < (len(list) - 2) / 2:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            max_index = index

            if list[left_child_index] > list[right_child_index] and list[left_child_index] > list[index]:
                max_index = left_child_index
            elif list[right_child_index] > list[left_child_index] and list[right_child_index] > list[index]:
                max_index = right_child_index
            if index != max_index:
                list[index], list[max_index] = list[max_index], list[index]
                self.sink(max_index, list)

    def build_max_heap(self, arr):
        if len(arr) > 1:
            index = len(arr) // 2 - 1 #首先，计算堆的最后一个非叶子节点的索引，这个索引是 (len(arr) // 2 - 1)。我们将从这个索引开始构建最大堆。
            for i in range(index + 1):
                self.sink(index, arr)
                index -= 1
        return arr


    def heap_sort(self, arr, root_list=None):
        """
1.交换根节点和最后一个节点：
最大堆的最大元素（根节点）现在位于堆的顶部，即数组的第一个位置。要排序数组，我们首先将根节点与数组的最后一个元素交换。这将确保最大的元素现在位于已排序部分的末尾。

2.减小堆的大小：
在完成第一步后，堆的大小（即数组的长度）减小了1，因为最大元素已经被放置到了正确的位置。这样，我们将堆的大小减小1，从而忽略了刚刚移动的最大元素。

3.重新调整堆：
现在，我们需要确保堆的剩余部分仍然是一个有效的最大堆。为此，我们需要进行下沉操作（sink），以便将新的根节点（原来的最后一个元素）移动到合适的位置，以满足最大堆的性质。

4.重复步骤 1-3：
重复执行步骤 1 到 3 直到堆的大小减小到1。每次执行步骤 1 时，将最大元素放到已排序部分的末尾，然后通过步骤 3 重新调整堆。这将逐渐建立一个已排序的部分，而堆的大小逐渐减小。

5.排序完成：
一旦堆的大小减小到1，排序完成。整个数组已经排好序，元素按照升序排列。

总结来说，堆排序的核心思想是将堆中的最大元素逐步提取出来，放到已排序部分的末尾，然后通过重新调整堆的操作，确保剩余部分仍然是一个有效的最大堆。这个过程一直持续，直到整个数组排好序。
        """
        if root_list == None:
            root_list = []
        n = len(arr)
        if n > 0:
            arr = self.build_max_heap(arr)
            arr[0], arr[-1] = arr[-1], arr[0]
            root_list.insert(0, arr[-1])
            arr.pop()
            self.heap_sort(arr, root_list)
            return arr + root_list



"""
写错了！！！
    def last_nonleaf_index(self, n=0, result=0):
        if result + 2**n <= len(self.heap_list) and result + 2**(n+1) > len(self.heap_list):
            return result + 2**n - 1
        else:
            return self.last_nonleaf_index(n+1, result+2**n)
"""


my_heap = Heap()

my_heap.insert(1)
my_heap.insert(3)
my_heap.insert(2)
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(8)
my_heap.insert(2.5)
my_heap.insert(0.5)
my_heap.insert(0.2)

print(my_heap.heap_list)

print(my_heap.delete_root())

print(my_heap.heap_list)

print(my_heap.build_max_heap([3,6,1,9,7,10,2,8,0]))

print(my_heap.heap_sort([3,6,1,9,7,10,2,8,0]))