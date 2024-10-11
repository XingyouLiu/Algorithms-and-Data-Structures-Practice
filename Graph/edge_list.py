from my_queue import Queue
from union_find import UnionFind
import random
import heapq

class EdgeListGraph:
    def __init__(self, directed):
        self.edges = []   # This will store tuples like (vertex1, vertex2) or (vertex1, vertex2, weight)
        self.vertices = set()   # This set stores all vertices
        self.directed =  directed

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, vertex_1, vertex_2, weight=None):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            raise ValueError
        if weight:
            edge = (vertex_1, vertex_2, weight)
        else:
            edge = (vertex_1, vertex_2)
        self.edges.append(edge)

    def has_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            raise ValueError
        return any((v1, v2) == (vertex_1, vertex_2) or (not self.directed and (v1, v2) == (vertex_2, vertex_1)) for v1, v2, *_ in self.edges)


    def remove_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            raise ValueError
        if self.has_edge(vertex_1, vertex_2):
            """
            以下代码为什么被删除？
            在遍历 self.edges 的同时也在修改它（通过移除元素）。这样做可能会导致运行时错误或者意外地跳过某些元素。
            常见的做法是先记录所有需要移除的边，然后在遍历之外的循环中移除它们。
            """
            """
            for edge in self.edges:
                if vertex_1 == edge[0] and vertex_2 == edge[1] or vertex_2 == edge[0] or vertex_2 == edge[1]:
                    self.edges.remove(edge)
            """
            to_remove = [(v1, v2) for v1, v2, *_ in self.edges if (v1, v2) == (vertex_1, vertex_2) or
                         (not self.directed and (v1, v2) == (vertex_2, vertex_1))]
            """
            对于每条边，*会收集边中除v1、v2以外余下的所有元素（如果有的话），比如说边的权重（如果存在）。
            下划线_是一个习惯用法，通常用来表示我们不打算使用的变量。所以，*_在这里的意思是“忽略边中除了起始顶点和结束顶点之外的所有元素。

            这样的写法确保了即使边是一个包含更多元素的元组（如在带权重的边中），循环也能正常工作，
            因为v1和v2总是分别指向第一个和第二个元素，而剩余的任何元素都会被放入*后面的变量（在这种情况下是_），而不会被使用。
            """
            for tuple_to_remove in to_remove:
                self.edges.remove(tuple_to_remove)


    def get_neighbors(self, vertex):
        if vertex not in self.vertices:
            raise ValueError
        neighbors_list = []
        for edge in self.edges:
            if vertex == edge[0]:
                neighbors_list.append(edge[1])
        return neighbors_list


    def get_edge_weight(self, vertex_1, vertex_2):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            raise ValueError
        if self.has_edge(vertex_1, vertex_2):
            for (v1, v2, *weight) in self.edges:  #*会收集边中除v1、v2以外余下的所有元素，*weight即为收集了除v1、v2以外余下的元素组成的元组
                if (v1, v2) == (vertex_1, vertex_2) or (not self.directed and (v1, v2) == (vertex_2, vertex_1)):
                    return weight[0] if weight else None
        raise ValueError


    def BFS(self, vertex):
        help_queue = Queue()
        if len(self.vertices) == 0:
            return []
        else:
            BFS_list = []
            visited = set()
            help_queue.enqueue(vertex)
            while not help_queue.is_empty():
                vertex = help_queue.dequeue()
                if vertex not in visited:
                    BFS_list.append(vertex)
                    visited.add(vertex)
                    for (v, *_) in self.get_neighbors(vertex):
                        if v not in visited:
                            help_queue.enqueue(v)
        return BFS_list

    """
    第一个版本（直接Bellman-Ford）：
时间复杂度：这个版本的时间复杂度为O(VE)，其中V是顶点数，E是边数。算法需要对所有边进行V-1次迭代。
空间复杂度：空间复杂度为O(V)，因为存储了所有顶点的距离和路径。
占用资源：这个版本没有预先使用BFS，所以直接跳到了对边的迭代，对所有顶点和边一视同仁。
    """
    def Bellman_Ford_1(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        routes = {vertex: [] for vertex in self.vertices}
        distances[start_vertex] = 0
        routes[start_vertex] = [start_vertex]

        v = len(self.vertices)
        for i in range(v - 1):
            is_distance_changed = False
            for (vertex_1, vertex_2, *weight) in self.edges:
                distance_1 = distances[vertex_1]
                distance_2 = distances[vertex_2]
                if distance_1 != float('infinity'):
                    if weight:
                        distance = distance_1 + weight[0]
                    else:
                        distance = distance_1 + 1
                    if distance < distance_2:
                        distances[vertex_2] = distance
                        routes[vertex_2] = routes[vertex_1] + [vertex_2]
                        is_distance_changed = True
            if is_distance_changed == False:
                break

        for (vertex_1, vertex_2, *weight) in self.edges:
            distance_1 = distances[vertex_1]
            distance_2 = distances[vertex_2]
            if distance_1 != float('infinity'):
                if weight:
                    distance = distance_1 + weight[0]
                else:
                    distance = distance_1 + 1
                if distance < distance_2:
                    raise ValueError('图中存在负权重循环！')

        return distances, routes

    """
    第二个版本（使用BFS优化）：
时间复杂度：BFS的时间复杂度是O(V+E)。对于Bellman-Ford部分，由于它只在BFS确定为可达的顶点上迭代，所以最坏情况下仍然是O(VE)，但实际上可能会因为跳过了一些不可达的顶点而有所改善。
空间复杂度：同样为O(V)，因为虽然使用了BFS，但存储距离和路径的空间需求没有变化。
占用资源：BFS会额外占用内存来存储队列，尤其是当图非常密集且大部分顶点都可达时。此外，如果图中大部分顶点都是可达的，那么BFS可能不会带来多少优化。
    """

    def Bellman_Ford_2(self, start_vertex):
        reachable_vertices = self.BFS(start_vertex)
        distances = {vertex: float('infinity') for vertex in self.vertices}
        routes = {vertex: [] for vertex in reachable_vertices}
        distances[start_vertex] = 0
        routes[start_vertex] = [start_vertex]

        v = len(reachable_vertices)
        for i in range(v - 1):
            is_distance_changed = False
            for (vertex_1, vertex_2, *weight) in self.edges:
                if vertex_1 in reachable_vertices:
                    distance_1 = distances[vertex_1]
                    distance_2 = distances[vertex_2]
                    if weight:
                        distance = distance_1 + weight[0]
                    else:
                        distance = distance_1 + 1
                    if distance < distance_2:
                        distances[vertex_2] = distance
                        routes[vertex_2] = routes[vertex_1] + [vertex_2]
                        is_distance_changed = True
            if is_distance_changed == False:
                break

        for (vertex_1, vertex_2, *weight) in self.edges:
            if vertex_1 in reachable_vertices:
                distance_1 = distances[vertex_1]
                distance_2 = distances[vertex_2]
                if weight:
                    distance = distance_1 + weight[0]
                else:
                    distance = distance_1 + 1
                if distance < distance_2:
                    raise ValueError('图中存在负权重循环！')

        return distances, routes

    """
总结：
如果图中不可达的顶点很少，或者大多数顶点都是可达的，那么第二个版本中的BFS可能不会带来显著的性能提升，因为大部分顶点仍然需要被Bellman-Ford算法处理。
如果图中有许多不可达的顶点，那么第二个版本可能会更高效，因为它避免了对这些顶点进行无用的迭代。
如果关心算法的最坏情况性能，那么两个版本在大型稠密图中的性能是相似的，因为Bellman-Ford算法的主要成本在于边的迭代，而不是顶点的可达性检查。
从实现的简洁性和理解的容易程度来看，第一个版本更直接、更清晰。除非你确定你的图中有大量的不可达顶点，并且这些不可达顶点显著影响了性能，否则没有必要进行BFS的预处理步骤。
在大多数情况下，我会推荐第一个版本，因为它更简单、更符合Bellman-Ford算法的直接应用，并且在大多数情况下，它的性能是足够的。
只有在特定情况下，当你确定图中有大量不可达的顶点，并且这些顶点对算法性能有显著影响时，才考虑使用第二个版本。
    """


    """
如下：
在循环外初始化一次优先队列，并且在每次迭代中只处理与最新加入MST的顶点相连的边（与之前加入MST的顶点相连的边，已经存在于优先队列中，无需再次加入了）：
这时优先队列中最多会有V-1个元素，因为最小生成树中有V个顶点，但在任何时候，从任何顶点到MST的边最多只有V-1条（这是在稠密图中的最坏情况，实际中通常会更少）。

因此，每次插入和删除操作的时间复杂度是O(log V)，而整个算法中所有边都会被处理，所以总的时间复杂度是O(E log V)。

在稀疏图中，E接近于V，这时O(E log V)和O(E log E)是相似的。
但在稠密图中，E可以达到V^2的数量级，这时O(E log V)显著优于O(E log E)。因此，通常推荐在循环外初始化优先队列，然后在每次迭代中更新优先队列的方法，以提高效率。   
    """
    def Prim(self, start_vertex):
        vertex_set = set()
        edge_set = set()
        vertex_set.add(start_vertex)
        pq = []
        while len(vertex_set) != len(self.vertices): #所有顶点都被加入MST顶点集合后，终止循环
            for vertex_prev in vertex_set: #遍历MST顶点集合中的每个顶点，查找链接该顶点与其他未加入MST集合的顶点的边
                for (vertex_1, vertex_2, weight) in self.edges: #在边列表中查找哪些边符合一端是MST集合中的某顶点，另一端是未加入MST集合的顶点，并将这些边添加进最小堆
                    if vertex_1 == vertex_prev:
                        if vertex_2 not in vertex_set:
                            heapq.heappush(pq, (weight, vertex_1, vertex_2))
            (weight, vertex_1, vertex_2) = heapq.heappop(pq) #在最小堆中取出最短的边，加入MST的边集合。并将这条最短边另一端的未加入MST集合的顶点，加入集合。
            edge_set.add((vertex_1, vertex_2, weight))  #最终结果是所有顶点都被加入MST的顶点集合，各顶点之间相对最短的边都被加入MST的边集合
            vertex_set.add(vertex_2)

        return edge_set, sum(weight for (v1, v2, weight) in edge_set)

    """
如下：
在Prim算法的每次迭代中都重新构建优先队列，那么每次迭代都涉及到将所有与MST中顶点相连的边插入优先队列中。
如果图中有E条边，那么对于每一轮插入操作，时间复杂度是O(log E)，因为每次插入操作都是在E条边中进行的。

由于每次迭代都需要对E条边进行插入操作，所以总的时间复杂度会是O(E log E)。
    """
    def Prim_worse_version(self, start_vertex):
        vertex_set = set()
        edge_set = set()
        vertex_set.add(start_vertex)
        while len(vertex_set) != len(self.vertices):
            pq = []
            for vertex_prev in vertex_set:
                for (vertex_1, vertex_2, weight) in self.edges:
                    if vertex_1 == vertex_prev:
                        if vertex_2 not in vertex_set:
                            heapq.heappush(pq, (weight, vertex_1, vertex_2))
            (weight, vertex_1, vertex_2) = heapq.heappop(pq)
            edge_set.add((vertex_1, vertex_2, weight))
            vertex_set.add(vertex_2)

        return edge_set, sum(weight for (v1, v2, weight) in edge_set)

    """
 Kruskal算法的时间复杂度：
 排序：Kruskal算法首先需要对所有边按照权重进行排序。这个操作的时间复杂度是 O(ElogE)，其中 E 是边的数量。
并查集操作：算法接下来需要对每条边进行处理，判断加入这条边是否会形成环。这涉及到并查集的查找和合并操作。并查集的查找和合并操作的时间复杂度在平均情况下可以近似为 O(α(N))，
其中 α 是阿克曼函数的逆函数，对于所有实际的输入规模 N，它都是一个非常小的常数（事实上，对于所有实际的输入规模，α 几乎不超过 4）。因此，对所有边进行处理的总时间复杂度大约是 O(Eα(N))。

综合这两部分，Kruskal算法的时间复杂度为 O(ElogE)+O(Eα(N))。由于 α(N) 是一个非常小的常数，可以近似地认为整体时间复杂度主要由边的排序决定，即 O(ElogE)。   
    """

    def Kruskal(self):
        union_find = UnionFind(self.vertices)
        reordered_edges = []
        for edge in self.edges:  #将self.edges中的所有边加入边的列表。但是为了按边的权重从小到大排序，将边中的元组中的元素重排顺序，将权重置于元组的第一位。
            v1, v2, weight = edge
            heapq.heappush(reordered_edges, (weight, v1, v2))
        MST_list = []
        union_time = 0 #记录并查集中合并操作的次数
        while union_time != len(self.vertices) - 1: #所有顶点都在并查集中属于同一个集合，无法继续合并时，终止循环。此时，合并操作刚好了进行N-1次，因为将N个元素合并为1个集合，刚好需要N-1次合并操作。
            if reordered_edges:
                edge = heapq.heappop(reordered_edges) #将边列表中的边，按照权重从小到大的顺序提取出来，进行处理
                weight, vertex_1, vertex_2 = edge
                if union_find.find(vertex_1) != union_find.find(vertex_2): #如果提取出的边，两个顶点在并查集里不属于同一个集合（不具有同一个代表元），则实施合并操作
                    union_find.union(vertex_1, vertex_2)
                    MST_list.append((vertex_1, vertex_2, weight)) #最终结果是，所有顶点都已被处理过（在并查集所有顶点都被合并进了同一个集合），且各顶点之间相对较短的边被加入了MST边集合
                    union_time += 1

        return MST_list, sum(weight for (vertex_1, vertex_2, weight) in MST_list)



    def get_edges_degrees_nondirected(self):
        degrees = {vertex: 0 for vertex in self.vertices}
        for edge in self.edges:
            vertex_1, vertex_2, *_ = edge
            degrees[vertex_1] += 1
            degrees[vertex_2] += 1
        return degrees

    def get_degree_ordered_vertices(self):
        degrees = self.get_edges_degrees_nondirected()
        return sorted(degrees, key=lambda v: degrees[v], reverse=True)

    def color(self):
        ordered_vertices = self.get_degree_ordered_vertices()
        color_dict = {vertex: 0 for vertex in ordered_vertices}
        for vertex in ordered_vertices:
            neighbor_list = self.get_neighbors(vertex)
            neighbor_color = [color_dict[vertex] for vertex in neighbor_list]
            color_choosed = 1
            while color_choosed in neighbor_color:
                color_choosed += 1
            color_dict[vertex] = color_choosed
        return color_dict

    """
贪心着色算法的时间复杂度分析：
假设图中有n个顶点，e条边
最坏情况：图是完全图（每一个顶点的度数（即相邻的顶点数）都为n-1）
1. 获取顶点的度数 (get_edges_degrees_nondirected): 此函数遍历所有边，因此其时间复杂度为 O(e)
2. 按度数排序顶点 (get_degree_ordered_vertices): 排序操作通常有 O(nlogn)的时间复杂度
3. 贪心着色 (color): 在这个函数中，对每个顶点进行了遍历，时间复杂度为O(n);
   对于每个顶点，又遍历了其所有邻接顶点来找出已使用的颜色。在最坏的情况下，每个顶点可能与所有其他顶点相邻，这会导致O(n)的时间复杂度；
   且，对于每个顶点，还需要在一个可能长达 n 的颜色列表中查找未使用的最小颜色，这也会导致O(n)的时间复杂度。
   由于后2个步骤是嵌套在顶点的遍历中，因此总体的时间复杂度为 O(n) * (O(n) + O(n))，最终结果为O(n^2)
因此，最坏情况的总体时间复杂度大概为：O(e) + O(nlogn) + O(n^2)，最终结果为 O(n^2)

然而，在大多数情况下，图不会是完全图,对于稀疏图（边数远小于 n^2 ), 或当图的结构使得邻接顶点的数量远小于 n 时，算法的实际运行时间可能会更短。

平均情况：
假设：1. 图不是完全图，顶点的平均度数远小于 n（图的顶点总数）。
     2. 图的结构不是特别规则，也就是说，没有特别的模式使得算法的性能显著下降。
排序顶点：排序顶点的时间复杂度仍然是 O(nlogn)。
为每个顶点着色：在平均情况下，每个顶点的邻接顶点数量会少于最坏情况下的 n−1。因此，遍历邻接顶点的时间复杂度会低于 O(n)。同样地，查找未使用的最小颜色的时间也会相应减少。

如果稀疏图（顶点的平均度数远小于顶点数量 n ，可以将平均度数视为为常数 k。）：
1.获取顶点的度数 (get_edges_degrees_nondirected): 此函数遍历所有边，因此其时间复杂度为 O(e)
2. 按度数排序顶点 (get_degree_ordered_vertices): 排序操作通常有 O(nlogn)的时间复杂度
3.3. 贪心着色 (color): 在这个函数中，对每个顶点进行了遍历，时间复杂度为O(n);
   对于每个顶点，又遍历了其所有邻接顶点来找出已使用的颜色，导致O(k)的时间复杂度；
   且，对于每个顶点，还需要在最大长度为k的颜色列表中查找未使用的最小颜色（因为度数为k的顶点有k个邻接顶点，最多有k种已使用颜色），这也会导致O(k)的时间复杂度。
   由于后2个步骤是嵌套在顶点的遍历中，因此总体的时间复杂度为 O(n) * (O(k) + O(k))，最终结果为O(kn)（等同于O(n))
因此，稀疏图情况的总体时间复杂度可能为：O(e) + O(nlogn) + O(n)，最终结果为 O(nlogn)
    
    """





my_graph = EdgeListGraph(True)

my_graph.add_vertex('0')

my_graph.add_vertex('1')

my_graph.add_vertex('2')

my_graph.add_vertex('3')

my_graph.add_vertex('4')

my_graph.add_edge('0', '1')

my_graph.add_edge('1', '0')

my_graph.add_edge('0','2', -2)

my_graph.add_edge('2','0', 2)

my_graph.add_edge('1','2', 3)

my_graph.add_edge('2','1', 3)

my_graph.add_edge('1','4', -4)

my_graph.add_edge('4','1', 4)

my_graph.add_edge('2','3', 5)

my_graph.add_edge('3','2', -5)

print(my_graph.Bellman_Ford_1('0'))

print(my_graph.Bellman_Ford_2('0'))


another_graph = EdgeListGraph(True)

another_graph.add_vertex('A')

another_graph.add_vertex('B')

another_graph.add_vertex('C')

another_graph.add_vertex('D')

another_graph.add_vertex('E')

another_graph.add_edge('A','B', 6)

another_graph.add_edge('B','A', 6)

another_graph.add_edge('A','D', -1)

another_graph.add_edge('D','A', 1)

another_graph.add_edge('B','D', -2)

another_graph.add_edge('D','B', 2)

another_graph.add_edge('B','C', 5)

another_graph.add_edge('C','B', 5)

another_graph.add_edge('C','E', 5)

another_graph.add_edge('E','C', 5)

another_graph.add_edge('B','E', 2)

another_graph.add_edge('E','B', 2)

another_graph.add_edge('D','E', 1)

another_graph.add_edge('E','D', 1)

print(another_graph.Bellman_Ford_1('A'))

print(another_graph.Bellman_Ford_2('A'))


weighted_nondirected_graph = EdgeListGraph(False)

weighted_nondirected_graph.add_vertex('A')

weighted_nondirected_graph.add_vertex('B')

weighted_nondirected_graph.add_vertex('C')

weighted_nondirected_graph.add_vertex('D')

weighted_nondirected_graph.add_edge('A', 'B', 2)

weighted_nondirected_graph.add_edge('B', 'A', 2)

weighted_nondirected_graph.add_edge('A', 'C', 6)

weighted_nondirected_graph.add_edge('C', 'A', 6)

weighted_nondirected_graph.add_edge('B', 'D', 3)

weighted_nondirected_graph.add_edge('D', 'B', 3)

weighted_nondirected_graph.add_edge('C', 'D', 1)

weighted_nondirected_graph.add_edge('D', 'C', 1)

print(weighted_nondirected_graph.Prim('A'))

print(weighted_nondirected_graph.Kruskal())

print(weighted_nondirected_graph.get_edges_degrees_nondirected())

print(weighted_nondirected_graph.color())


"""
语法说明：
1. 
在Python中，星号*被用作一个特殊的操作符，它在这里的使用场景是"unpacking"（解包）。
在函数调用或其他赋值操作中，*操作符可以用来收集多余的位置参数，而**操作符可以用来收集多余的关键字参数。

a, b, *rest = [1, 2, 3, 4, 5]
在上面这个例子中，a将被赋值为1，b将被赋值为2，而剩下的值3, 4, 5将作为列表被赋值给rest。

2. 
a if condition else b
这个表达式的意思是：如果condition为真，表达式的结果是a；如果为假，表达式的结果是b。

3.
生成器表达式：
假设我们有一个需求，要对列表中的每个元素求平方，如果使用列表推导式，我们会这样写：
squares = [x**2 for x in range(10)]

如果我们改用生成器表达式，可以写成：
squares_gen = (x**2 for x in range(10))

使用生成器表达式的优点是，如果列表非常大，使用列表推导式会一次性创建整个列表，消耗大量内存，而生成器表达式则是按需计算每个元素，内存效率更高。

如何使用生成器对象：
生成器表达式返回的生成器对象可以通过 next() 函数来逐个访问元素：
next(squares_gen)  # 输出第一个元素：0
next(squares_gen)  # 输出第二个元素：1

也可以通过循环来迭代所有元素：
for square in squares_gen:
    print(square)
    
需要注意的是，生成器是一次性使用的，一旦消耗完毕，再次尝试从中获取元素会引发 StopIteration 异常。

4.
any() 是一个内置函数，在 Python 中用来检查可迭代对象（比如列表、元组、集合等）中是否至少有一个元素为真值（True）。
如果是这样的话，any() 就会返回 True；否则，如果可迭代对象为空或者所有元素都为假值（False），它会返回 False。
any() 函数在处理大数据集时尤其有用，因为它在遇到第一个“真值”时会立即返回，而不需要评估整个数据集，这提高了效率。
举例：
print(any(x**2 > 10 for x in range(4)))  # 输出：False，因为 0^2, 1^2, 2^2, 3^2 都不大于 10
print(any(x**2 > 10 for x in range(5)))  # 输出：True，因为 4^2 = 16 大于 10
"""