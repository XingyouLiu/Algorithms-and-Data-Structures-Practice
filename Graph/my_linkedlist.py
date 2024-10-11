class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.point_tail = None   #指向末尾元素的指针
        self.size = 0   #元素个数计数器

    def is_empty(self):
        return self.head == None


    def append(self, value):
        append_node = Node(value=value)
        if self.is_empty():
            self.head = append_node
        else:
            current = self.head
            while current.next:
                current=current.next
            current.next = append_node
        self.point_tail = append_node
        self.size += 1


    def insert(self, value, position):
        insert_node = Node(value=value)
        if self.is_empty() and position == 0:
            self.head = insert_node
        elif position == 0:
            insert_node.next = self.head
            self.head = insert_node
        else:
            current = self.head
            for i in range(position-1):
                current = current.next
                if current == None:
                    raise IndexError('Index out of range!')
            insert_node.next = current.next
            current.next = insert_node
            if insert_node.next == None:
                self.point_tail = insert_node
        self.size += 1


    def delete(self, position):
        if self.is_empty():
            raise ValueError('This is an empty linkedlist!')
        elif position == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            current = self.head
            previous = None
            for i in range(position):
                previous = current
                current = current.next
                if current == None:
                    raise IndexError('Index out of range!')
            previous.next = current.next
            self.size -= 1
            if previous.next == None:
                self.point_tail = previous


    def delete_value(self, value):
        """
        删除第一个值为value的节点
        """
        if self.is_empty():
            raise ValueError('This is an empty linkedlist!')
        elif self.head.value == value:
            self.head = self.head.next
            self.size -= 1
        else:
            current = self.head
            previous = None
            while current:
                if current.value == value:
                    previous.next = current.next
                    if previous.next == None:
                        self.point_tail = previous
                    self.size -= 1
                    break
                previous = current
                current = current.next
            if current == None:
                raise ValueError('No value found in linkedlist!')


    def reverse(self):
        """
        双指针技术：有current、previous两个指针。2个指针在循环中同步向后移动。previous总是在current前一个位置。
        本段代码原理是：将链表中每一个元素原本指向后一个元素的.next，转变为指向前一个元素。最后，将指针最终指向的元素（即原本的最后一个元素）转换为头节点
        """
        self.point_tail = self.head
        current = self.head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


    def traversal(self):
        printed_list = []
        current = self.head
        if self.is_empty():
            return printed_list
        else:
            while current:
                printed_list.append(current.value)
                current=current.next
        return printed_list


    def clear(self):
        self.head = None
        self.point_tail = None
        self.size = 0