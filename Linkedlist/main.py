class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

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

    def insert(self, value, position):
        insert_node = Node(value=value)
        if self.is_empty() and position == 0:
            self.head = insert_node
        elif position == 0:
            insert_node.next = self.head
            self.head = insert_node
        else:
            i=0
            is_i_equal_to_position = False
            current = self.head
            while current.next:
                i += 1
                if i == position:
                    is_i_equal_to_position = True
                    break
                current = current.next
            if is_i_equal_to_position == False and i < position - 1:
                raise IndexError('Index out of range!')
            else:
                insert_node.next = current.next
                current.next = insert_node

    def insert_simplified_version(self, value, position):
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

    def delete(self, position):
        if self.is_empty():
            raise ValueError('This is an empty linkedlist!')
        elif position == 0:
            self.head = self.head.next
        else:
            i=0
            is_i_equal_to_position = False
            current = self.head
            while current.next:
                i += 1
                if i == position:
                    is_i_equal_to_position = True
                    current.next = current.next.next
                    break
                current = current.next
            if is_i_equal_to_position == False:
                raise IndexError('Index out of range!')

    def delete_simplified_version(self, position):
        if self.is_empty():
            raise ValueError('This is an empty linkedlist!')
        elif position == 0:
            self.head = self.head.next
        else:
            current = self.head
            previous = None
            for i in range(position):
                previous = current
                current = current.next
                if current == None:
                    raise IndexError('Index out of range!')
            previous.next = current.next



    def delete_value(self, value):
        """
        删除第一个值为value的节点
        """
        if self.is_empty():
            raise ValueError('This is an empty linkedlist!')
        elif self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            previous = None
            while current:
                if current.value == value:
                    previous.next = current.next
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


linked_list = LinkedList()

linked_list.append(1)

linked_list.append(2)

linked_list.append(3)

linked_list.append(5)

linked_list.insert_simplified_version(value=6, position=3)

print(f'linklist insert: {linked_list.traversal()}')

linked_list.delete_simplified_version(position=4)

print(f'linklist delete position: {linked_list.traversal()}')

linked_list.reverse()

print(f'linklist reverse: {linked_list.traversal()}')

linked_list.delete_value(value=3)

print(f'linklist delete value: {linked_list.traversal()}')