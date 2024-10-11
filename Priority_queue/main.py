from heap import Heap

class PriorityQueue():
    def __init__(self):
        self.priority_queue = Heap()

    def is_empty(self):
        return self.priority_queue.is_empty()

    def enqueue(self, value):
        self.priority_queue.insert(value)

    def extract_max(self):
        return self.priority_queue.delete_root()

    def get_max(self):
        if self.priority_queue.is_empty():
            return None
        else:
            return self.priority_queue.heap_list[0]

    def size(self):
        return len(self.priority_queue.heap_list)

    def clear(self):
        while not self.priority_queue.is_empty():
            self.priority_queue.heap_list.pop()


priority_queue = PriorityQueue()

priority_queue.enqueue(3)

priority_queue.enqueue(8)

priority_queue.enqueue(10)

priority_queue.enqueue(1)

priority_queue.enqueue(2)

print(priority_queue.get_max())

print(priority_queue.extract_max())

print(priority_queue.extract_max())

print(priority_queue.size())

priority_queue.clear()

print(priority_queue.size())