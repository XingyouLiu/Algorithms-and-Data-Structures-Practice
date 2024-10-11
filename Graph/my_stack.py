from my_linkedlist import Node, LinkedList

class Stack():
    def __init__(self):
        self.linkedlist = LinkedList()

    def is_empty(self):
        return self.linkedlist.is_empty()

    def push(self, value):
        self.linkedlist.append(value)

    def pop(self):
        if self.is_empty():
            raise ValueError('This is an empty stack!')
        else:
            pop_value = self.linkedlist.point_tail.value
            last_index = self.linkedlist.size - 1
            self.linkedlist.delete(last_index)
            return pop_value

    def peek(self):
        if self.is_empty():
            raise ValueError('This is an empty stack!')
        else:
            return self.linkedlist.point_tail.value


    def size(self):
        return self.linkedlist.size

    def clear(self):
        self.linkedlist.clear()

