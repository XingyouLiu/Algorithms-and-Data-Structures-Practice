from my_linkedlist import Node, LinkedList

class Queue():
    def __init__(self):
        self.linkedlist = LinkedList()

    def enqueue(self, value):  #将元素添加至队列的末尾
        self.linkedlist.append(value)

    def dequeue(self):  #从队列的前端移除并返回一个元素
        if self.is_empty():
            raise ValueError('The queue is empty!')
        front_value = self.linkedlist.head.value
        self.linkedlist.delete(position=0)
        return front_value

    def peek(self):   #返回队列前端的元素，但不从队列中删除它
        if self.is_empty():
            raise ValueError('The queue is empty!')
        return self.linkedlist.head.value

    def is_empty(self):
        return self.linkedlist.is_empty()

    def size(self):
        return self.linkedlist.size

    def clear(self):
        self.linkedlist.clear()
