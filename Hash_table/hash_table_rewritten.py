class HashTable():
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(self.size)]


    def hash_function(self, key):
        return hash(key) % self.size


    def insert(self, key, value):
        """
        插入操作首先计算键的哈希值来找到对应的索引。
        如果该索引对应的位置为空，则直接存储键值对；
        如果不为空，根据链地址法来处理这个键值对，在该索引处的链表或数组中添加新的键值对。
        """
        index = self.hash_function(key)
        # Check if the key exists, replace old key-value pair with new one:
        for i, (k, v) in enumerate(self.table[index]):
            if key == k:
                self.table[index][i] = (key, value)
                return
        # Check if the key doesn't exist, add key-value pair to the list corresponding to the index:
        self.table[index].append((key, value))


    def get(self, key):
        index = self.hash_function(key)
        for (k, v) in self.table[index]:
            if key == k:
                return v
        raise KeyError('Key Does Not Exist!')


    def search(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for (k, v) in self.table[index]:
                if k == key:
                    return True
        return False


    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for i, (k, v) in enumerate(self.table[index]):
                if key == k:
                    self.table[index].pop(i)
                    return v
        raise KeyError('Key Does Not Exist!')



hash_table = HashTable(10)

hash_table.insert(key='diana',value=100)

hash_table.insert(key='haoren',value=99.5)

print(hash_table.get('diana'))

print(hash_table.remove('haoren'))

hash_table.get('xiaoming')