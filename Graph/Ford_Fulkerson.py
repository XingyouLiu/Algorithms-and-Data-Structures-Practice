from edge_list import EdgeListGraph
import heapq


"""
回溯：
回溯是一种常用于解决递归问题的技术，特别是在涉及到搜索和探索（如搜索所有可能的解决方案）的情境中。在编程中，回溯通常指的是在递归过程中“回退”到上一个状态，以探索不同的可能性或路径。

回溯的关键步骤：
选择：从一系列选项中选择一个选项进行尝试。
探索：基于当前的选择，继续前进以解决问题的剩余部分。
回退：如果当前选择无法达到最终的解决方案或满足条件，那么回退到上一步，撤销当前的选择，并尝试其他选项。

回溯的应用示例：
想象一个迷宫游戏，您要找到从起点到终点的路径。可以使用回溯算法来尝试不同的路径：
选择一个方向走：比如向北。
继续前进：沿选定的方向走，直到遇到死路或终点。
如果遇到死路，回退：如果向北走不通，则回到选择点，改为向东走。
"""

"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
以下的find_one_path 和 find_all_paths 写法有错！！！！！！！！！！！！！！！！！！！！！
错在递归的基线条件设置不对！基线条件不应该是：当前顶点已无任何邻接顶点 ！而应该是：当前顶点的所有邻接顶点都已存在于visited中，也即此条路径走到了尽头，没有新的未访问顶点可继续深入查找了！
正确版本详见 adjacent_matrix_graph_rewritten.py 中的写法！！！！！！！！！！！！！！！！！
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
"""
以下写法有错！！！！！！！！！！！！！！！！！！
find_all_paths是一个递归函数，用于在图中找到从 start_vertex（起始顶点）到 end_vertex（终点）的所有路径。它使用了回溯算法的原则来探索所有可能的路径。

初始化：函数开始时，将当前顶点设置为起始顶点，初始化路径（path）、路径列表（paths_list）和一个记录已访问顶点的集合（visited）。

标记当前顶点：将当前顶点(currrent_vertex)添加到路径中，并标记为已访问。

检查终点：如果当前顶点是终点，就将当前路径(path)添加到路径列表(paths_list)中。

探索邻接顶点：如果当前顶点不是终点，且当前顶点有邻居：函数将遍历其所有未访问的邻接顶点，并对每个邻接顶点递归调用自身。（即，将每个邻接顶点作为起始顶点，寻找它到终点的路径）

回溯：如果当前顶点是终点，则回溯寻找其他通往终点的路径；若当前顶点不是终点，且当前顶点已经没有任何邻接顶点，也还是需要回溯，寻找能够通往终点的路径。
如何回溯：撤销对当前顶点的访问（即从路径path中移除该顶点），并将其标记为未访问（即从已访问中移除）。这是回溯的关键步骤，它允许函数在探索完一条路径后回退并尝试其他替代路径。

返回结果：最终，函数返回包含所有从起点到终点的路径的列表。
"""
def find_all_paths(graph, start_vertex, end_vertex, path=None, paths_list=None, visited=None):
    current_vertex = start_vertex
    if path == None:
        path = []
    if paths_list == None:
        paths_list = []
    if visited == None:
        visited = set()

    visited.add(current_vertex)
    path.append(current_vertex)

    if current_vertex == end_vertex:
        paths_list.append(path.copy())
    else:
        if graph.get_neighbors(current_vertex):
            for (v, *_) in graph.get_neighbors(current_vertex):
                if v not in visited:
                    find_all_paths(graph, v, end_vertex, path, paths_list, visited)

    path.pop()
    visited.remove(current_vertex)
    return paths_list


"""
以下写法有错！！！！！！！！！！！！！！！！！！
find_one_path是一个递归函数，用于在图中找到从 start_vertex（起始顶点）到 end_vertex（终点）的其中一条路径。同样使用了回溯算法的原则，以及深度优先搜索的思想。
"""
def find_one_path(graph, start_vertex, end_vertex, path=None, visited=None):
    current_vertex = start_vertex
    if path == None:
        path = []
    if visited == None:
        visited = set()
    path.append(current_vertex)
    visited.add(current_vertex)
    if current_vertex == end_vertex:
        return path   #若当前顶点就是要寻找的终点，则立刻返回本条路径
    else:
        if graph.get_neighbors(current_vertex): #如果当前顶点不是要寻找的终点，且当前顶点还有可以继续深入查找的邻接顶点，则继续深入递归查找
            for (v, *_) in graph.get_neighbors(current_vertex):
                if v not in visited:
                    return find_one_path(graph, v, end_vertex, path, visited)
        else:  #如果当前顶点并不是要寻找的终点，且当前顶点已经没有任何邻接顶点可供继续深入，则回溯到上一个顶点
            path.pop()
            visited.remove(current_vertex)
    return path


"""
BFS并不是常用的获取图中从起点到终点所有路径的方式，因为它可能会造成很大的时间和空间复杂度。
如果图中有环，尝试用 BFS 找到所有路径的方法可能会陷入死循环，或者至少会生成大量重复的或无限长的路径。这是因为在存在环的图中，同一个顶点可以通过不同的路径多次到达，从而创建循环路径。

避免死循环的方法
1. 记录已访问路径：为了避免死循环，可以在每条路径中记录已经访问过的顶点。当准备将一个顶点添加到路径中时，先检查它是否已经在该路径中出现过。如果是，那么您应该跳过这个顶点，以避免创建循环路径。

2. 限制路径长度：另一种方法是限制路径的最大长度。例如，您可以设置路径长度不得超过图中顶点总数的某个倍数。这可以防止创建无限长的路径，但可能会错过一些有效的路径。

3. DFS配合回溯算法，才是获取所有路径的最常用方式，不会因为图中有环而陷入死循环。因为DFS会剔除访问过的顶点，使之不会反反复复地在路径中出现。
"""
"""
用BFS获取图中所有路径，需要对原本的BFS做出重大修改，否则将反复地访问已寻找到的路径中的顶点，造成死循环。

1. 需要使用队列和已访问集合存储路径，而不是仅存储顶点，队列应该存储到达每个顶点的路径。这意味着队列中的每个元素都是一条路径（顶点列表）。
并且，要将获取到的路径加入已访问的路径集合，防止重复获取同一条路径。

2. 扩展路径：当处理队列中的一条路径时，检查路径末尾顶点的所有邻居。对于每个邻居，如果它不是终点，创建一条新的路径（在当前路径的基础上加上这个邻居），然后将这条新路径加入队列。

3. 处理终点：如果路径末尾的邻居是终点，那么就找到了一条从起点到终点的路径。将这条路径记录下来，并继续处理队列中的其他路径。

4. 避免重复路径：由于队列中存储的是路径而非单个顶点，所以每个顶点可能会以不同的路径被多次访问。这正是找到所有路径所需要的。

举例：
假设您的图是这样的：A -> B -> C 和 A -> C。
当 BFS 开始时，队列是 [[A]]。
处理路径 [A] 时，您发现 A 的邻居有 B 和 C，所以队列变成了 [[A, B], [A, C]]。
接下来处理路径 [A, B]，发现 B 的邻居是 C，所以添加新路径 [A, B, C]。
"""
def find_all_paths_BFS(graph, start_vertex, end_vertex):
    paths_list = []

    current_vertex = start_vertex

    help_queue = [tuple([current_vertex])]
    path = ()

    while help_queue and len(path) <= 2 * len(graph.vertices):
        path = ()
        visited = set()
        current_path = help_queue.pop(0)
        current_vertex = current_path[-1]
        if current_path not in visited:
            visited.add(current_path)
            if graph.get_neighbors(current_vertex):
                for (v, *_) in graph.get_neighbors(current_vertex):
                    if current_path + tuple([v]) not in visited:
                        help_queue.append(current_path + tuple([v]))

                    if end_vertex in graph.get_neighbors(v):
                        path = current_path + (v, end_vertex)
                        help_queue.append(path)
                        visited.add(path)
                        paths_list.append(path)


    return paths_list




def Ford_Fulkerson(graph, start_vertex, end_vertex, path=None, visited=None, each_edge_flow=None, each_path_flow=None):
    current_vertex = start_vertex
    if path == None:
        path = []
    if visited == None:
        visited = set()
    if each_edge_flow == None:
        each_edge_flow={(vertex_1, vertex_2): weight for (vertex_1, vertex_2, weight) in graph.edges}
    if each_path_flow == None:
        each_path_flow = dict()

    visited.add(current_vertex)
    path.append(current_vertex)

    if len(path) >= 2:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)] #将当前path所包含的每条边都以（边起点，边终点）的形式提取到path_edges列表中
        path_edges_flow = [each_edge_flow[edge] for edge in path_edges] #获取当前path每条边当前剩余的流量

    if current_vertex == end_vertex: #假如找到了一条增广路径（能够由源点到达汇点的路径）
        path_max_flow = min(path_edges_flow) #让这条增广路径的最大流量等于这条路径上流量最小的边能够容纳的流量
        for (edge, flow) in each_edge_flow.items(): #遍历（边：流量）字典，以寻找出当前路径上的每条边，并改变其流量（原流量 - 赋予给现路径的最大流量）
            if edge in path_edges:
                each_edge_flow[edge] -= path_max_flow
        each_path_flow[tuple(path)] = path_max_flow #存储当前增广路径的流量
    else: #假如尚未找到增广路径，则继续探索当前顶点的邻居，向更深处寻找
        if graph.get_neighbors(current_vertex):
            for v in graph.get_neighbors(current_vertex):
                if v not in visited: #如果当前路径尚未包含邻居顶点，则访问邻居顶点，避免重复访问导致死循环
                    if each_edge_flow[(current_vertex, v)] > 0: #如果从当前顶点到邻居顶点之间的边上尚有剩余流量：
                        Ford_Fulkerson(graph, v, end_vertex, path, visited, each_edge_flow, each_path_flow) #对每个邻接顶点递归调用自身。（即，将每个邻接顶点作为起始顶点，寻找它到终点的增广路径）

    path.pop()
    visited.remove(current_vertex)
    return each_path_flow


def Edmonds_Karp(graph, start_vertex, end_vertex):
    each_edge_flow = {(vertex_1, vertex_2): weight for (vertex_1, vertex_2, weight) in graph.edges}
    each_path_flow = dict()

    while True: #循环直到无法找到新的增广路径：使用 while True 来进行循环，并在找不到新的增广路径时通过 if path == []: break 来跳出循环。
        current_vertex = start_vertex
        visited = set()
        parent_vertex_of_visited = {}
        help_queue = [current_vertex]
        path = []
        while help_queue: #使用 BFS 寻找增广路径：通过队列 help_queue 和集合 visited 实现 BFS，以及使用字典 parent_vertex_of_visited 来记录路径，这些都是 BFS 的标准实现方法。
            current_vertex = help_queue.pop(0)
            if current_vertex not in visited:
                visited.add(current_vertex)
                for (v, *_) in graph.get_neighbors(current_vertex):
                    if v not in visited:
                        if each_edge_flow[(current_vertex, v)] > 0: #检查了 each_edge_flow[(current_vertex, v)] > 0 来确定是否可以沿着该边继续寻找路径。
                            help_queue.append(v)
                            parent_vertex_of_visited[v] = current_vertex

                    if v == end_vertex:
                        path = []   #找到增广路径后，逆向重建了路径
                        path.append(v)
                        while v in parent_vertex_of_visited:
                            path.append(parent_vertex_of_visited[v])
                            v = parent_vertex_of_visited[v]
                        path.reverse()

                        if len(path) >= 2:
                            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
                            path_edges_flow = [each_edge_flow[edge] for edge in path_edges]

                        path_max_flow = min(path_edges_flow)  #计算了路径上的最小流量 path_max_flow
                        for (edge, flow) in each_edge_flow.items(): #正确地只更新了路径上的边的流量
                            if edge in path_edges:
                                each_edge_flow[edge] -= path_max_flow #维护了 each_edge_flow 来跟踪每条边的流量，并在 each_path_flow 中记录了每条找到的路径及其流量。
                        each_path_flow[tuple(path)] = path_max_flow
                        break

        if path == []:
            break

    return each_path_flow





my_graph = EdgeListGraph(True)

my_graph.add_vertex('S')
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('T')

my_graph.add_edge('S', 'A' , 10)
my_graph.add_edge('S', 'B' , 10)
my_graph.add_edge('A', 'C' , 4)
my_graph.add_edge('B', 'C' , 6)
my_graph.add_edge('B', 'T' , 7)
my_graph.add_edge('C', 'A' , 3)
my_graph.add_edge('C', 'T' , 10)


another_graph = EdgeListGraph(True)
another_graph.add_vertex('S')
another_graph.add_vertex('A')
another_graph.add_vertex('B')
another_graph.add_vertex('C')
another_graph.add_vertex('T')
another_graph.add_edge('S', 'A' , 10)
another_graph.add_edge('S', 'B' , 10)
another_graph.add_edge('A', 'C' , 4)
another_graph.add_edge('B', 'C' , 6)
another_graph.add_edge('B', 'T' , 7)
another_graph.add_edge('C', 'T' , 10)

print(find_one_path(graph=my_graph, start_vertex='S', end_vertex='T'))

print(find_all_paths(my_graph, 'S', 'T'))

print(find_all_paths_BFS(my_graph, 'S', 'T'))

print(find_all_paths_BFS(another_graph, 'S', 'T'))

print(f"F:{Ford_Fulkerson(my_graph, 'S', 'T')}")

print(f"E:{Edmonds_Karp(my_graph, 'S', 'T')}")



