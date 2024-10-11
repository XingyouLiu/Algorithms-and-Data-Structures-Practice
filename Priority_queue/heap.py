class Heap():
    def __init__(self, heap_type='max'):
        self.heap_list = []
        self.heap_type = heap_type

    def is_empty(self):
        return len(self.heap_list) == 0

    def wrong_insert(self, value, list_left=None, list_right=None):
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
        self.heap_list.append(value)
        self.heapify_up(index = len(self.heap_list)-1)

    def heapify_up(self, index):
        if index != 0:
            parent_index = (index-1) // 2
            if self.heap_list[parent_index] < self.heap_list[index]:
                self.heap_list[parent_index], self.heap_list[index] = self.heap_list[index], self.heap_list[parent_index]
                self.heapify_up(parent_index)


    def delete_root(self):
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
            index = len(arr) // 2 - 1
            for i in range(index + 1):
                self.sink(index, arr)
                index -= 1
        return arr


    def heap_sort(self, arr, root_list=None):
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