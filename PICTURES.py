import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()  # создаём объект графа

# определяем список узлов (ID узлов)

nodes = ["1", "2", "3", "4", "5", "4'", "5'","5''"]

# определяем спиок рёбер
# список кортежей, каждый из которых представляет ребро
# кортеж (id_1, id_2) означает, что узлы id_1 и id_2 соединены ребром
edges = [("1","2"), ("1","4"), ("2","3"), ("2","5'"), ("1","5"), ("3","4'"), ("4'","5''")]
# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos = nx.circular_layout(G)
options = {
    'node_color': ['crimson','crimson','crimson','lightpink','lightpink','lightpink','crimson','crimson'],
    'node_size': 3500,          # size of node
    'width': 1,                 # line width of edges
    'arrowstyle': '-|>',        # array style for directed graph
    'arrowsize': 10,            # size of arrow
    'edge_color':'black',        # edge color
}
nx.draw(G, pos, with_labels = True, **options)
nx.draw_networkx_edge_labels(G, 
	 pos,
    edge_labels={ ("1","2"):'(1)', ("1","4"):'(2)', ("2","3"):'(4)', ("2","5'"):'(5)', ("1","5"):'(30)', ("3","4'"):'(6)', ("4'","5''"):'(7)'
,
    },
    font_color='crimson'
)
plt.show()