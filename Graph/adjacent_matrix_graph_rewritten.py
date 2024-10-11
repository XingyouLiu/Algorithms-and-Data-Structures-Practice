import heapq


class AdjacentMatrixGraph():
    def __init__(self, directed = False):
        self.adj_matrix = []
        self.num_vertices = 0
        self.vertices_name_list = []
        self.vertices_name_index_map = {}
        self.is_directed = directed


    def add_vertex(self, vertex_name):
        if vertex_name in self.vertices_name_list:
            raise ValueError(f'Vertex: {vertex_name} has already existed!')
        self.vertices_name_list.append(vertex_name)
        self.vertices_name_index_map[vertex_name] = self.num_vertices
        if self.num_vertices == 0:
            self.adj_matrix.append([0])
        else:
            for i in range(self.num_vertices):
                self.adj_matrix[i].append(0)
            self.adj_matrix.append([0 for _ in range(self.num_vertices + 1)])
        self.num_vertices += 1


    def add_edge(self, vertex_1_name, vertex_2_name, weight = None):
        if weight == None:
            weight = 1
        if vertex_1_name in self.vertices_name_list and vertex_2_name in self.vertices_name_list:
            vertex_1_index = self.vertices_name_index_map[vertex_1_name]
            vertex_2_index = self.vertices_name_index_map[vertex_2_name]
            if not self.is_directed:
                self.adj_matrix[vertex_2_index][vertex_1_index] = weight
            self.adj_matrix[vertex_1_index][vertex_2_index] = weight
        else:
            raise ValueError('One or both vertices do not exist.')


    def remove_edge(self, vertex_1_name, vertex_2_name):
        if vertex_1_name in self.vertices_name_list and vertex_2_name in self.vertices_name_list:
            vertex_1_index = self.vertices_name_index_map[vertex_1_name]
            vertex_2_index = self.vertices_name_index_map[vertex_2_name]
            if not self.is_directed:
                self.adj_matrix[vertex_2_index][vertex_1_index] = 0
            self.adj_matrix[vertex_1_index][vertex_2_index] = 0
        else:
            raise ValueError('One or both vertices do not exist.')


    def has_edge(self, vertex_1_name, vertex_2_name):
        if vertex_1_name in self.vertices_name_list and vertex_2_name in self.vertices_name_list:
            vertex_1_index = self.vertices_name_index_map[vertex_1_name]
            vertex_2_index = self.vertices_name_index_map[vertex_2_name]
            return self.adj_matrix[vertex_1_index][vertex_2_index] != 0 or self.adj_matrix[vertex_2_index][vertex_1_index] != 0
        else:
            raise ValueError('One or both vertices do not exist.')


    def print_graph(self):
        for row in self.adj_matrix:
            print(row)


    def get_neighbors(self, vertex_name):
        if vertex_name in self.vertices_name_list:
            vertex_index = self.vertices_name_index_map[vertex_name]
            neighbors_index = [tuple([i]) for i, edge in enumerate(self.adj_matrix[vertex_index]) if edge == 1] + [(i, edge_weight) for i, edge_weight in enumerate(self.adj_matrix[vertex_index]) if edge_weight != 0 and edge_weight != 1]
            neighbors_names = [name for name, index in self.vertices_name_index_map.items() if index in [index for (index, *_) in neighbors_index]]
            return neighbors_index, neighbors_names
        raise ValueError('Vertex does not exist!')


    def DFS(self, vertex_name):
        if vertex_name in self.vertices_name_list:
            if self.num_vertices == 1:
                return [vertex_name]
            else:
                return self.DFS_help(vertex_name)

    def DFS_help(self, current, visited_set = None, output_list = None):
        if visited_set == None:
            visited_set = set()
        if output_list == None:
            output_list = []

        if current not in visited_set:
            output_list.append(current)
            visited_set.add(current)
            neighbors_index, neighbors_names = self.get_neighbors(current)
            for vertex in neighbors_names:
                self.DFS_help(vertex, visited_set, output_list)

        return output_list


    def DFS_loop(self, vertex_name):
        if vertex_name in self.vertices_name_list:
            if self.num_vertices == 1:
                return [vertex_name]
            else:
                visited_set = set()
                output_list = []
                help_stack = [vertex_name]
                while help_stack:
                    current = help_stack.pop()
                    if current not in visited_set:
                        output_list.append(current)
                        visited_set.add(current)
                        neighbors_index, neighbors_names = self.get_neighbors(current)
                        help_stack += neighbors_names
                        #代码将所有邻居添加到栈中，而不管它们是否已经被访问过。尽管这不会影响最终结果，但可能会导致队列中包含重复的顶点，进而影响效率。
                        #可以多写一个for循环遍历neighbors，在将邻居添加进stack之前检查其是否被访问过，且只添加未被访问的邻居进栈。
                return output_list


    def BFS(self, vertex_name):
        if vertex_name in self.vertices_name_list:
            if self.num_vertices == 1:
                return [vertex_name]
            else:
                visited_set = set()
                output_list = []
                help_queue = [vertex_name]
                while help_queue:
                    current = help_queue.pop(0)
                    if current not in visited_set:
                        output_list.append(current)
                        visited_set.add(current)
                        neighbors_index, neighbors_names = self.get_neighbors(current)
                        help_queue += neighbors_names
                return output_list


    def find_one_path(self, current, end_vertex, path = None, visited = None):
        if path == None:
            path = []
        if visited == None:
            visited = set()
        path.append(current)
        visited.add(current)
        if current == end_vertex:
            return path
        else:
            neighbors_index, neighbors_names = self.get_neighbors(current)
            for neighbor in neighbors_names:
                if neighbor not in visited:
                    result = self.find_one_path(neighbor, end_vertex, path, visited)
                    if result != None:
                        return result
            path.pop()
            visited.remove(current)
            return None


    def find_all_paths(self, current, end_vertex, path = None, visited = None, paths_list = None):
        if path == None:
            path = []
        if visited == None:
            visited = set()
        if paths_list == None:
            paths_list = []
        path.append(current)
        visited.add(current)
        if current == end_vertex:
            paths_list.append(path.copy())
        else:
            neighbors_index, neighbors_names = self.get_neighbors(current)
            for neighbor in neighbors_names:
                if neighbor not in visited:
                    self.find_all_paths(neighbor, end_vertex, path, visited, paths_list)
        path.pop()
        visited.remove(current)
        return paths_list



    def Dijkstra(self, start_vertex):
        """
        时间复杂度为 V * O(logV) + E * O(logV) = O((V+E)logV)
        """
        min_distances = {vertex: float('infinity') for vertex in self.vertices_name_list}
        routes = {vertex: [] for vertex in self.vertices_name_list}
        min_distances[start_vertex] = 0
        routes[start_vertex] = [start_vertex]
        visited = set()

        priority_queue = [(0, start_vertex)]
        while len(visited) != self.num_vertices: #循环最多执行 V 次。因为每次循环处理一个顶点并将其加入已访问。一个顶点一旦被访问，就不会再次被处理。
            current = heapq.heappop(priority_queue)[1] #heappop的时间复杂度为O(logN)，因此该步骤时间复杂度为O(logV)
            if current not in visited:
                neighbors_index, neighbors_names = self.get_neighbors(current)
                for (neighbor, weight) in neighbors_index: #在整个算法执行全过程中，该循环总共进行E次（在全过程中，遍历所有顶点的所有邻接顶点，其总数即为所有顶点出度的总和，即为总边数）
                    if min_distances[current] + weight < min_distances[str(neighbor)]:
                        min_distances[str(neighbor)] = min_distances[current] + weight
                        routes[str(neighbor)] = routes[current] + [str(neighbor)]
                visited.add(current)
                for vertex, distance in min_distances.items():
                    heapq.heappush(priority_queue, (distance, vertex)) #heappush的的时间复杂度为O(logN)，因此该步骤时间复杂度为O(logV)

        return min_distances, routes


    def Bellman_Ford(self, start_vertex):
        """
        时间复杂度为 O(VE)（最多V次松弛操作，每次松弛操作中都遍历所有边），显著高于Dijkstra的时间复杂度，因此通常只将Bellman_Ford应用于存在负权重边的场景
        """
        distances = {vertex: float('infinity') for vertex in self.vertices_name_list}
        routes = {vertex: [] for vertex in self.vertices_name_list}
        distances[start_vertex] = 0
        routes[start_vertex] = [start_vertex]

        for i in range(self.num_vertices - 1):
            is_distance_changed = self.relaxation(start_vertex, distances, routes)
            if not is_distance_changed:
                break

        is_distance_changed = self.relaxation(start_vertex, distances, routes)
        if is_distance_changed:
            raise ValueError('图中存在负权重循环！')
        return distances, routes

    def relaxation(self, start_vertex, distances, routes, is_distance_changed = False):
        for vertex in self.vertices_name_list:
            neighbors_index, neighbors_names = self.get_neighbors(vertex)
            for i, (neighbor_index, weight) in enumerate(neighbors_index):
                neighbor = neighbors_names[i]
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
                    routes[neighbor] = routes[vertex] + [neighbor]
                    is_distance_changed = True
        return is_distance_changed




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

print(my_graph.DFS('4'))

print(my_graph.DFS('3'))

print(my_graph.DFS('1'))

print(my_graph.DFS_loop('0'))

print(my_graph.DFS_loop('4'))

print(my_graph.DFS_loop('3'))

print(my_graph.BFS('1'))

print(my_graph.BFS('0'))

print(f"my_graph Dijstra: {my_graph.Dijkstra('0')}")

print(my_graph.find_one_path('2', '3'))

print(my_graph.find_all_paths('0', '3'))



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


