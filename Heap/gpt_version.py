class MaxHeap:
    def __init__(self):
        self.heap = []

    """
    插入操作（heappush）：时间复杂度为O(logN)
添加元素：新元素被加到堆的末尾（数组的末尾），这是O(1)的操作。
调整堆：然后，新元素会按照堆的属性向上移动，直到它小于其父节点或者已经移动到堆的顶部。这个过程叫做“上浮”（heapify up）。
在最坏的情况下，“上浮”过程可能需要遍历堆的整个高度，对于完全二叉树来说，树的高度是log N（其中N是堆中元素的数量）。因此，这个过程是O(log N)的。
    """
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    """
上浮操作时间复杂度为O(logN) (因为在最坏的情况下，“上浮”过程可能需要遍历堆的整个高度，对于完全二叉树来说，树的高度是log N（其中N是堆中元素的数量））
    """
    def heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    """
    删除最小元素操作（heappop）：时间复杂度为O(logN)
移除元素：堆顶元素（数组的第一个元素，也是最小的元素）被移除，这是O(1)的操作。
调整堆：通常会将最后一个元素移动到堆顶，然后进行“下沉”（heapify down）操作，以保持堆的特性。元素会与其子节点比较，如果不满足堆的性质，则与其较小的子节点交换位置，这个过程持续到元素比其所有子节点都小，或者已经移动到叶子节点。
与插入操作一样，“下沉”过程最多需要遍历堆的高度，即O(log N)。
    """
    def delete_root(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink(0)
        return root

    """
    下沉操作时间复杂度为O(logN) (因为在最坏的情况下，“下沉”过程可能需要遍历堆的整个高度，对于完全二叉树来说，树的高度是log N（其中N是堆中元素的数量））
    """
    def sink(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        largest = idx

        if (left_child_idx < len(self.heap) and
                self.heap[left_child_idx] > self.heap[largest]):
            largest = left_child_idx

        if (right_child_idx < len(self.heap) and
                self.heap[right_child_idx] > self.heap[largest]):
            largest = right_child_idx

        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self.sink(largest)

    """
需要格外留意：建堆（将无序的输入数组建立成一个最大堆（或最小堆））的时间复杂度是 O(N) ！！！其中 N 是数组中的元素数量。
需要格外留意，尽管每次插入操作是 O(log N)，但是建堆操作可以通过一种称为“下沉”（heapify down）的方法以线性时间完成。
乍一看，建堆操作似乎需要对每个元素都进行下沉操作，而每次下沉操作的时间复杂度为 O(log N)，那么对所有 N 个元素进行下沉操作的总时间复杂度似乎应该是 O(N log N)。
然而，实际上建堆的时间复杂度确实是 O(N) ！！！

解释：
对于一个完全二叉树，最底层有大约 N/2 个叶子节点，它们不需要下沉；
上一层有 N/4 个节点，每个节点最多下沉 1 次；
再上一层有 N/8 个节点，每个节点最多下沉 2 次；
以此类推，直到根节点。
我们可以通过求和来计算这个系数：总的下沉操作次数 ≤ N/4 * 1 + N/8 * 2 + N/16 * 3 + ... + 1 * log N。 这个系数通常是小于 1 的一个常数。
写为积分形式，约为：积分 h(k) dk 从 k=1 到 k=log(N)
当 N 趋向于无穷大时，这个积分的结果趋向于一个常数！

要注意的是，这个分析是对完全二叉树的平均情况进行的分析，它说明了在实际操作中建堆的效率远高于直观上的 O(N log N)。
    """
    def build_max_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self.sink(i)
        return arr

    """
堆排序的时间复杂度为O(NlogN),即N乘以删除堆中最大元素的时间复杂度O(logN)。因为本质上，堆排序是要经历N次将堆中最大元素弹出，加入排序后的列表。
    """
    def heap_sort(self):
        sorted_arr = []
        while len(self.heap) > 0:
            sorted_arr.append(self.delete_root())
        return sorted_arr

# 示例用法
my_heap = MaxHeap()

my_heap.insert(1)
my_heap.insert(3)
my_heap.insert(2)
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(8)
my_heap.insert(2.5)
my_heap.insert(0.5)
my_heap.insert(0.2)

print(my_heap.heap)

print(my_heap.delete_root())

print(my_heap.heap)

print(my_heap.build_max_heap([3,6,1,9,7,10,2,8,0]))

print(my_heap.heap_sort())