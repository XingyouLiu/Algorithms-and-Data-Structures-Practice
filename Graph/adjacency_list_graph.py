from my_queue import Queue

class AdjacencyListGraph:
    def __init__(self, directed = False):
        self.directed = directed
        self.adj_list = {}
        self.num_vertices = 0

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.num_vertices += 1


    def add_edge(self, vertex_1, vertex_2, weight=None):
        if vertex_1 == vertex_2:
            raise KeyError
        if vertex_1 not in self.adj_list or vertex_2 not in self.adj_list:
            raise KeyError
        if weight:
            self.adj_list[vertex_1].append((vertex_2, weight))
            if not self.directed:
                self.adj_list[vertex_2].append((vertex_1, weight))
        else:
            self.adj_list[vertex_1].append((vertex_2))
            if not self.directed:
                self.adj_list[vertex_2].append((vertex_1))


    def remove_edge(self, vertex_1, vertex_2):
        if vertex_1 == vertex_2:
            raise KeyError
        if vertex_1 not in self.adj_list or vertex_2 not in self.adj_list:
            raise KeyError
        for (vertex, *_) in self.adj_list[vertex_1]:
            if vertex_2 == vertex:
                self.adj_list[vertex_1].remove(vertex_2)
                break
        if not self.directed:
            for (vertex, *_) in self.adj_list[vertex_2]:
                if vertex_1 == vertex:
                    self.adj_list[vertex_2].remove(vertex_1)
                    break


    def has_edge(self, vertex_1, vertex_2):
        if vertex_1 == vertex_2:
            raise KeyError
        if vertex_1 not in self.adj_list or vertex_2 not in self.adj_list:
            raise KeyError
        for (vertex, *_) in self.adj_list[vertex_1]:
            if vertex_2 == vertex:
                return True
        return False


    def get_neighbors(self, vertex):
        if vertex not in self.adj_list:
            raise KeyError
        return self.adj_list[vertex]


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


my_graph = AdjacencyListGraph(True)

my_graph.add_vertex('0')

my_graph.add_vertex('1')

my_graph.add_vertex('2')

my_graph.add_vertex('3')

my_graph.add_vertex('4')

my_graph.add_edge('0', '1')

my_graph.add_edge('1', '0')

my_graph.add_edge('0','2', 2)

my_graph.add_edge('2','0', 2)

my_graph.add_edge('1','2', 3)

my_graph.add_edge('2','1', 3)

my_graph.add_edge('1','4', 4)

my_graph.add_edge('4','1', 4)

my_graph.add_edge('2','3', 5)

my_graph.add_edge('3','2', 5)

print(my_graph.get_neighbors('0'))

print(my_graph.DFS('0'))

print(my_graph.DFS_traversal('0'))

print(my_graph.BFS('1'))