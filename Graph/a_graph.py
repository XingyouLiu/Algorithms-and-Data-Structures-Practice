import matplotlib.pyplot as plt
import networkx as nx

# 创建一个空的有向图
G = nx.DiGraph()

# 添加顶点
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')

# 添加带有权重的边
G.add_edge('A', 'B', weight=6)
G.add_edge('A', 'D', weight=1)
G.add_edge('B', 'A', weight=6)
G.add_edge('B', 'C', weight=5)
G.add_edge('B', 'D', weight=2)
G.add_edge('B', 'E', weight=2)
G.add_edge('C', 'B', weight=5)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'A', weight=1)
G.add_edge('D', 'B', weight=2)
G.add_edge('D', 'E', weight=1)
G.add_edge('E', 'B', weight=2)
G.add_edge('E', 'C', weight=5)
G.add_edge('E', 'D', weight=1)

# 绘制图形
pos = nx.spring_layout(G)  # 生成一个布局以便我们的图可视化更加美观
weights = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

# 显示图形
plt.show()
