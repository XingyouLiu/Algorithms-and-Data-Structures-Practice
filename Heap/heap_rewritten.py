class MinHeap():
    def __init__(self):
        self.heap = []


    def is_empty(self):
        return len(self.heap) == 0


    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(index = len(self.heap) - 1)


    def heapify_up(self, index):
        if index != 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                self.heapify_up(parent_index)


    def delete_root(self):
        if self.is_empty():
            raise ValueError('Empty Heap!')
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            original_root = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.sink(index = 0)
            return original_root


    def sink(self, index):
        if index <= (len(self.heap) - 3) / 2:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_item_index = index

            if self.heap[left_child_index] < self.heap[right_child_index] and self.heap[left_child_index] < self.heap[index]:
                smallest_item_index = left_child_index
            elif self.heap[right_child_index] < self.heap[left_child_index] and self.heap[right_child_index] < self.heap[index]:
                smallest_item_index = right_child_index

            if index != smallest_item_index:
                self.heap[index], self.heap[smallest_item_index] = self.heap[smallest_item_index], self.heap[index]
                self.sink(smallest_item_index)


    def build_min_heap(self, array):
        """
        首先，计算堆的最后一个非叶子节点的索引，这个索引是 (len(arr) // 2 - 1)。我们将从这个索引开始，向着堆顶层的方向，对每个元素进行下沉操作。
        """
        self.heap = array
        last_nonleaf_index = len(array) // 2 - 1
        current_index = last_nonleaf_index
        if len(array) > 1:
            for i in range(last_nonleaf_index + 1):
                self.sink(current_index)
                current_index -= 1
        return self.heap


    def heap_sort(self, array, sorted_list = None):
        """
        因为最小堆的根节点一定是最小值，因此只需先将数组转换为最小堆，然后重复n次删除根节点操作（包含了用sink进行重新堆化的操作）（并将已删除的根节点加入排序后列表）
        """
        if sorted_list == None:
            sorted_list = []
            self.build_min_heap(array)
        if len(array) > 0:
            sorted_list.insert(0, self.delete_root())
            self.heap_sort(self.heap, sorted_list)
        return sorted_list

    def heap_sort_1(self, array, sorted_list = None):
        if sorted_list == None:
            sorted_list = []
            self.build_min_heap(array)
        if len(array) > 0:
            sorted_list.insert(0, self.heap[0])
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap.pop()
            self.heap_sort_1(self.heap, sorted_list)
        return sorted_list




my_heap = MinHeap()

my_heap.insert(1)
my_heap.insert(3)
my_heap.insert(2)
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(8)
my_heap.insert(2.5)
my_heap.insert(0.5)
my_heap.insert(0.2)

print(my_heap.heap)

print(my_heap.delete_root())

print(my_heap.heap)

print(my_heap.build_min_heap([3,6,1,9,7,10,2,8,0]))

print(my_heap.heap_sort([3,6,1,9,7,10,2,8,0]))

