class Node():
    def __init__(self, value = None):
        self.next = None
        self.value = value


class LinkedList():
    def __init__(self):
        self.head = None
        self.point_tail = None
        self.size = 0


    def is_empty(self):
        return self.head == None


    def append(self, value):
        append_node = Node(value)
        if self.is_empty():
            self.head = append_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = append_node
        self.point_tail = append_node
        self.size += 1


    def insert(self, value, position):
        insert_node = Node(value)
        if position == 0:
            if self.size == 0:
                self.head = insert_node
            else:
                insert_node.next = self.head
                self.head = insert_node
        else:
            if position > self.size:
                raise IndexError('Index out of range!')
            current = self.head
            for i in range(position - 1):
                current = current.next
            insert_node.next = current.next
            current.next = insert_node
            if insert_node.next == None:
                self.point_tail = insert_node
        self.size += 1


    def delete(self, position):
        if self.size == 0:
            raise ValueError('This is an empty linkedlist!')
        if position == 0:
            self.head = self.head.next
        else:
            if position > self.size - 1:
                raise IndexError('Index out of range!')
            current = self.head
            for i in range(position - 1):
                current = current.next
            current.next = current.next.next
            if current.next == None:
                self.point_tail = current
        self.size -= 1


    def delete_value(self, value):
        """
        删除第一个值为value的节点
        """
        if self.size == 0:
            raise ValueError('This is an empty linkedlist!')
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    if current.next == None:
                        self.point_tail = current
                    break
                current = current.next
                if current.next == None:
                    raise IndexError('Index out of range!')
        self.size -= 1


    def reverse(self):
        self.point_tail = self.head
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


    def traversal(self):
        output_list = []
        if self.size == 0:
            return output_list
        current = self.head
        while current:
            output_list.append(current.value)
            current = current.next
        return output_list


    def clear(self):
        self.head = None
        self.point_tail = None
        self.size = 0



linked_list = LinkedList()

linked_list.append(1)

linked_list.append(2)

linked_list.append(3)

linked_list.append(5)

print(f'linklist traversal: {linked_list.traversal()}')

linked_list.insert(value=6, position=3)

print(f'linklist insert: {linked_list.traversal()}')

linked_list.delete(position=4)

print(f'linklist delete position: {linked_list.traversal()}')

linked_list.reverse()

print(f'linklist reverse: {linked_list.traversal()}')

linked_list.delete_value(value=3)

print(f'linklist delete value: {linked_list.traversal()}')