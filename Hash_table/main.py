class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        """
        插入操作首先计算键的哈希值来找到对应的索引。
        如果该索引对应的位置为空，则直接存储键值对；
        如果不为空，根据链地址法来处理这个键值对，在该索引处的链表或数组中添加新的键值对。
        """
        index = self.hash_function(key)
        #Check if the key exists:
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        #if the key doesn't exist:
        self.table[index].append((key, value))

    def get(self, key):
        """
        获取操作也是计算键的哈希值来找到索引，然后根据存储的结构来查找实际的值。如果发生碰撞，并且使用了链地址法，则需要遍历链表来查找正确的值。
        """
        index = self.hash_function(key)
        if self.table[index]:
            for (k, v) in self.table[index]:
                if k == key:
                    return v
        raise KeyError

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for (k, v) in self.table[index]:
                if k == key:
                    return True
        return False

    def remove(self, key):
        index = self.hash_function(key)
        #Check if the key exists:
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return v
        #if the key doesn't exist:
        raise KeyError


hash_table = HashTable(10)

hash_table.insert(key='diana',value=100)

hash_table.insert(key='haoren',value=99.5)

print(hash_table.get('diana'))

print(hash_table.remove('haoren'))

hash_table.get('xiaoming')
