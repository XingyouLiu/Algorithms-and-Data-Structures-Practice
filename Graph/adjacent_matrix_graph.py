from my_queue import Queue
import heapq

class AdjacentMatrixGraph:
    def __init__(self, directed = False):
        self.adj_matrix = []
        self.num_vertices = 0
        self.directed_or_not = directed
        self.vertex_map = {}
        self.vertex_name_list = []

    def add_vertex(self, vertex_name):
        if vertex_name:
            if vertex_name in self.vertex_name_list:
                print(f"Vertex {vertex_name} already exists.")
                return
            self.vertex_map[vertex_name] = len(self.vertex_name_list)
            self.vertex_name_list.append(vertex_name)
        if self.adj_matrix == []:
            self.adj_matrix.append([0])
        else:
            for i in range(self.num_vertices):
                self.adj_matrix[i].append(0)
            self.adj_matrix.append([0 for _ in range(self.num_vertices+1)])
        self.num_vertices += 1


    def add_edge(self, vertex_1_name, vertex_2_name, weight=None):
        if vertex_1_name in self.vertex_name_list and vertex_2_name in self.vertex_name_list:
            if weight:
                if not self.directed_or_not:
                    self.adj_matrix[self.vertex_map[vertex_2_name]][self.vertex_map[vertex_1_name]] = weight
                self.adj_matrix[self.vertex_map[vertex_1_name]][self.vertex_map[vertex_2_name]] = weight
            else:
                if not self.directed_or_not:
                    self.adj_matrix[self.vertex_map[vertex_2_name]][self.vertex_map[vertex_1_name]] = 1
                self.adj_matrix[self.vertex_map[vertex_1_name]][self.vertex_map[vertex_2_name]] = 1
        else:
            print("One or both vertices do not exist.")
            return


    def remove_edge(self, vertex_1_name, vertex_2_name):
        if vertex_1_name in self.vertex_name_list and vertex_2_name in self.vertex_name_list:
            if not self.directed_or_not:
                self.adj_matrix[self.vertex_map[vertex_2_name]][self.vertex_map[vertex_1_name]] = 0
            self.adj_matrix[self.vertex_map[vertex_1_name]][self.vertex_map[vertex_2_name]] = 0
        else:
            raise IndexError


    def has_edge(self, vertex_1, vertex_2):
        if vertex_1 < self.num_vertices and vertex_2 < self.num_vertices:
            return self.adj_matrix[vertex_1][vertex_2] != 0
        else:
            print("One or both vertices do not exist.")
            return


    def print_graph(self):
        for row in self.adj_matrix:
            print(row)


    def get_neighbors(self, vertex_name):
        neighbors_list = []
        for i, edge in enumerate(self.adj_matrix[self.vertex_map[vertex_name]]):
            if edge != 0:
                if edge == 1:
                    neighbors_list.append((self.vertex_name_list[i]))
                else:
                    neighbors_list.append((self.vertex_name_list[i], edge))
        return neighbors_list


    def DFS(self, vertex):
        if self.num_vertices == 0:
            return []
        else:
            DFS_list = []
            visited = set()
            help_stack = [vertex]
            while help_stack:
                vertex = help_stack.pop()
                if vertex not in visited:
                    DFS_list.append(vertex)
                    visited.add(vertex)
                    if self.get_neighbors(vertex):
                        for (v, *_) in self.get_neighbors(vertex):
                            if v not in visited:
                                help_stack.append(v)
            return DFS_list


    def DFS_traversal(self, vertex):
        if self.num_vertices == 0:
            return []
        else:
            return self.DFS_traversal_help(vertex)

    def DFS_traversal_help(self, vertex, DFS_list=None, visited=None):
        if DFS_list == None:
            DFS_list = []
        if visited == None:
            visited = set()
        if vertex not in visited:
            DFS_list.append(vertex)
            visited.add(vertex)
            for (v, *_) in self.get_neighbors(vertex):
                self.DFS_traversal_help(vertex=v, DFS_list=DFS_list, visited=visited)
        return DFS_list


    def BFS(self, vertex):
        help_queue = Queue()
        if self.num_vertices == 0:
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


    def dijkstra(self, start_vertex):
        reachable_vertices = self.BFS(start_vertex) #广度优先搜索时间复杂度为O(V+E)
        visited_vertices = set()
        distances = {vertex: float('infinity') for vertex in reachable_vertices}
        routes = {vertex: [] for vertex in reachable_vertices}
        distances[start_vertex] = 0
        routes[start_vertex] = [start_vertex]
        pq = [(0, start_vertex)]
        while pq: #循环最多执行 V 次，因为一个顶点一旦被访问，就不会再次被处理
            current_distance, current_vertex = heapq.heappop(pq) #heappop时间复杂度为O(log n)，n为堆中元素数量，因此该步骤时间复杂度为O(log V)
            if current_vertex not in visited_vertices: #python的集合是基于散列表实现的，在集合中查找、添加、删除元素时间复杂度均为O(1)
                visited_vertices.add(current_vertex)
                neighbors = self.get_neighbors(current_vertex)
                """
                检查某顶点的所有邻接顶点。注意，以下循环在整个算法的执行过程中，总共进行E次。（而并非在while pq的每一次循环中都进行E次。次数E是分配于while pq的所有循环次数中的。）
                """
                for (neighbor_vertex, *weight) in neighbors: #检查某顶点的所有邻接顶点。
                    if neighbor_vertex not in visited_vertices:
                        if weight:
                            distance = current_distance + weight[0]
                        else:
                            distance = current_distance + 1
                        if distance < distances[neighbor_vertex]:
                            distances[neighbor_vertex] = distance
                            routes[neighbor_vertex] = routes[current_vertex] + [neighbor_vertex]
                            heapq.heappush(pq, (distance, neighbor_vertex)) #heappush时间复杂度为O(log n)，n为堆中元素数量，因此该步骤时间复杂度为O(log V)
                        """
                        为什么以下两句条件判断语句可以直接剔除？
                        想象：若distance > distance[neighbor_vertex]，意味着neighbor_vertex这个顶点的距离在此前已经更新过（因此变成不是无穷大），
                        意味着neighbor_vertex和它当前的距离，在此前已经经历过被加入优先队列（可能没有从优先队列中被取出过，但是优先队列中存在它）
                        因此，没有必要再次将neighbor_vertex和它当前的距离再次加入优先队列！
                        
                        此外，优先队列中的确可能会存在同一顶点、距离不同的多个元组。但是，当把顶点及其最小距离的元组从优先队列中取出后，我们就已得到该顶点的最小距离，
                        并将顶点标记为已处理，后续无需再次访问或处理它，更无需更新它的距离。因为，在第一次将顶点从优先队列取出时，就已经得到了它的最小距离！
                        因此，虽然后续的过程中，我们可能仍会将顶点及其对应的非最小距离从优先队列取出，但由于顶点已存在于已处理集合中，我们将会直接跳过这些后来取出的元组，不会进行任何操作！
                        
                        为什么当第一次将顶点从优先队列取出时，就已经得到了它的最小距离？
                        Dijkstra算法的贪心策略是：在每一步中，总是选择当前已知的最短路径顶点进行处理。
                        最短路径的确定性：当一个顶点从优先队列中取出时，它的最短路径已经确定，因为此时它的距离是所有未处理顶点中最短的。
                                       按照算法的逻辑，没有其他路径能够提供更短的距离到这个顶点，因为任何其他路径都会经过一个具有更长已知距离的顶点。

                        优先队列的作用：优先队列（最小堆）保证了每次都是当前已知最短距离的顶点被处理。这意味着任何通过尚未处理的顶点的路径都不可能比当前已知的路径更短。
                        """
                        #else:
                            #heapq.heappush(pq, (distances[neighbor_vertex], neighbor_vertex))

        return distances, routes


    def Bellman_Ford(self, start_vertex):
        """
        不用边列表，而是用邻接矩阵实现Bellman Ford算法时，无需将邻接矩阵中的边都专门提取出来，存储于列表中。
        直接用get_neighbors方法获取某顶点与哪些顶点之间有边、它们之间边的权重分别是多少，即可相当于把边都提取出来了。
        """
        distances = {vertex: float('infinity') for vertex in self.vertex_name_list}
        routes = {vertex: [] for vertex in self.vertex_name_list}
        distances[start_vertex] = 0
        routes[start_vertex] = [start_vertex]

        v = len(self.vertex_name_list)
        for i in range(v - 1):
            is_distance_changed = False
            for vertex_1 in self.vertex_name_list:
                for (vertex_2, *weight) in self.get_neighbors(vertex_1):
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

        for vertex_1 in self.vertex_name_list:
            for (vertex_2, *weight) in self.get_neighbors(vertex_1):
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
在Python中，heapq模块实现的是一个最小堆（min-heap）。因此，堆的顶部（即堆数组的第一个元素）总是最小的元素。

在Python的heapq模块中，当元组被用作堆中的元素时，元组中的第一项用作比较的主要依据。如果第一项相同，那么它会比较第二项，以此类推。

当使用heapq.heappush()添加元素到堆时，它会保持最小堆的性质，即确保数组的第一个元素始终是整个堆中最小的元素。
对应地，当使用heapq.heappop()从堆中弹出元素时，它会弹出并返回数组中的第一个元素，即堆中最小的元素，并确保剩余元素重新组成最小堆。

在Dijkstra算法和其他很多图算法中，我们通常关注的是找到“最小”成本、距离或权重，这就是为什么最小堆在这些场景中非常有用。

如果你需要一个最大堆（max-heap），你可以通过简单的技巧来实现：
即在元素插入堆之前，对值取相反数，弹出时再次取相反数即可。这样，本质上最小的数（取反后的最大数）就会在堆顶，从而模拟出“最大堆”的行为。
"""

"""
    通常不会使用递归来实现广度优先搜索（BFS）。
    BFS的本质是按层（按宽度）遍历图，这通常通过使用队列（queue）数据结构在循环中实现。使用队列可以确保首先访问每个节点的所有直接邻居，然后再移至下一层的邻居。
    这与递归的深度优先搜索（DFS）相反，DFS利用调用栈，深入到可能的最远路径，然后回溯。
    递归是以深度优先的方式工作的，因为当你递归调用一个函数时，你会继续深入到新的层级，直到达到某种基本情况（比如图的末端）。
    这与BFS的层级方式不一致，因此在实现BFS时通常不使用递归。
    如果你尝试使用递归实现BFS，你可能会面临很大的困难，并且它将违背BFS的基本原则。
    而且，这样做可能会导致不必要的复杂性和效率问题。在大多数情况下，使用队列的迭代方法将是实现BFS的最佳选择。
"""



"""
0 - 1 - 4
| /
2 - 3
"""





my_graph = AdjacentMatrixGraph(True)

my_graph.add_vertex('0')

my_graph.add_vertex('1')

my_graph.add_vertex('2')

my_graph.add_vertex('3')

my_graph.add_vertex('4')

my_graph.add_edge('0', '1', 3)

my_graph.add_edge('1', '0', 3)

my_graph.add_edge('0','2', 2.5)

my_graph.add_edge('2','0', 2)

my_graph.add_edge('1','2', 3)

my_graph.add_edge('2','1', 3)

my_graph.add_edge('1','4', 4.5)

my_graph.add_edge('4','1', 4)

my_graph.add_edge('2','3', 5)

my_graph.add_edge('3','2', 5)

my_graph.print_graph()

print(my_graph.get_neighbors('1'))

print(my_graph.DFS('0'))

print(my_graph.DFS_traversal('0'))

print(my_graph.BFS('1'))

print(f"my_graph Dijstra: {my_graph.dijkstra('0')}")


my_graph1 = AdjacentMatrixGraph(True)

my_graph1.add_vertex('0')

my_graph1.add_vertex('1')

my_graph1.add_vertex('2')

my_graph1.add_vertex('3')

my_graph1.add_vertex('4')

my_graph1.add_edge('0', '1')

my_graph1.add_edge('1', '0')

my_graph1.add_edge('0','2', -2)

my_graph1.add_edge('2','0', 2)

my_graph1.add_edge('1','2', 3)

my_graph1.add_edge('2','1', 3)

my_graph1.add_edge('1','4', -4)

my_graph1.add_edge('4','1', 4)

my_graph1.add_edge('2','3', 5)

my_graph1.add_edge('3','2', -5)

print(my_graph1.Bellman_Ford('0'))


another_graph = AdjacentMatrixGraph(True)

another_graph.add_vertex('A')

another_graph.add_vertex('B')

another_graph.add_vertex('C')

another_graph.add_vertex('D')

another_graph.add_vertex('E')

another_graph.add_edge('A','B', 6)

another_graph.add_edge('B','A', 6)

another_graph.add_edge('A','D', 1)

another_graph.add_edge('D','A', 1)

another_graph.add_edge('B','D', 2)

another_graph.add_edge('D','B', 2)

another_graph.add_edge('B','C', 5)

another_graph.add_edge('C','B', 5)

another_graph.add_edge('C','E', 5)

another_graph.add_edge('E','C', 5)

another_graph.add_edge('B','E', 2)

another_graph.add_edge('E','B', 2)

another_graph.add_edge('D','E', 1)

another_graph.add_edge('E','D', 1)

print(f"another_graph Dijstra: {another_graph.dijkstra('A')}")


another_graph1 = AdjacentMatrixGraph(True)

another_graph1.add_vertex('A')

another_graph1.add_vertex('B')

another_graph1.add_vertex('C')

another_graph1.add_vertex('D')

another_graph1.add_vertex('E')

another_graph1.add_edge('A','B', 6)

another_graph1.add_edge('B','A', 6)

another_graph1.add_edge('A','D', -1)

another_graph1.add_edge('D','A', 2)

another_graph1.add_edge('B','D', -2)

another_graph1.add_edge('D','B', 2)

another_graph1.add_edge('B','C', 5)

another_graph1.add_edge('C','B', 5)

another_graph1.add_edge('C','E', 5)

another_graph1.add_edge('E','C', 5)

another_graph1.add_edge('B','E', 2)

another_graph1.add_edge('E','B', 2)

another_graph1.add_edge('D','E', 3)

another_graph1.add_edge('E','D', 3)

print(another_graph1.Bellman_Ford('A'))
