class MaxHeap():
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        if index != 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                self.heapify_up(parent_index)

    def delete_root(self):
        if self.heap == []:
            raise ValueError
        elif len(self.heap) == 1:
            return self.heap.pop()
        original_root = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.sink(0)
        return original_root

    def sink(self, index):
        if self.heap == []:
            raise ValueError
        elif len(self.heap) == 1:
            return self.heap

        size = len(self.heap)
        r_child_index, l_child_index = 2 * index + 2, 2 * index + 1

        # 确保子节点索引没有超出范围
        if l_child_index < size:
            max_value = max(self.heap[l_child_index], self.heap[index])
            if r_child_index < size:
                max_value = max(max_value, self.heap[r_child_index])

            if self.heap[index] != max_value:
                if self.heap[l_child_index] == max_value:
                    self.heap[index], self.heap[l_child_index] = self.heap[l_child_index], self.heap[index]
                    if l_child_index <= (len(self.heap) - 1) // 2:
                        self.sink(l_child_index)

                elif r_child_index < size and self.heap[r_child_index] == max_value:
                    self.heap[index], self.heap[r_child_index] = self.heap[r_child_index], self.heap[index]
                    if r_child_index <= (len(self.heap) - 1) // 2:
                        self.sink(r_child_index)

    def build_heap(self, array):
        new_heap = MaxHeap()
        new_heap.heap = array
        if len(array) > 1:
            index = (len(new_heap.heap) - 1) // 2
            while index >= 0:
                new_heap.sink(index)
                index -= 1
        return new_heap.heap

    def heap_sort(self, heap):
        new_heap = MaxHeap()
        new_heap.heap = heap
        length = len(heap)
        return self.heap_sort_help(None, 0, length, new_heap)

    def heap_sort_help(self, sorted_part, i, length, heap):
        if sorted_part == None:
            sorted_part = []
        if i < length:
            sorted_part.append(heap.delete_root())
            sorted_part = self.heap_sort_help(sorted_part, i + 1, length, heap)
        return sorted_part


a_heap = MaxHeap()
new_heap = a_heap.build_heap([5,1,4,2,3])
print(new_heap)
print(a_heap.heap_sort(new_heap))