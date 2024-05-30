import snap
from scipy.sparse import lil_matrix
 
def get_valid_start_node(num_nodes):
    while True:
        print(f"Введите номер стартовой вершины от 1 до {num_nodes}:")
        start = int(input())
        if 1 <= start <= num_nodes:
            return start - 1  # Возвращаем индекс, начинающийся с 0
        else:
            print("Номер вершины должен быть в диапазоне от 1 до", num_nodes)
def get_valid_end_node(num_nodes):
    while True:
        print(f"Введите номер конечной вершины от 1 до {num_nodes}:")
        end = int(input())
        if 1 <= end <= num_nodes:
            return end - 1  # Возвращаем индекс, начинающийся с 0
        else:
            print("Номер вершины должен быть в диапазоне от 1 до", num_nodes)
 
# Load the graph
G = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)
num_nodes = G.GetNodes()
n = num_nodes
 
# Create a mapping of node IDs to indices
node_id_to_index = {}
index = 0
for node in G.Nodes():
    node_id_to_index[node.GetId()] = index
    index += 1
 
# Create the adjacency matrix
matrix = lil_matrix((num_nodes, num_nodes))
 
# Populate the adjacency matrix
for EI in G.Edges():
    src_index = node_id_to_index[EI.GetSrcNId()]
    dst_index = node_id_to_index[EI.GetDstNId()]
    matrix[src_index, dst_index] = 1
    matrix[dst_index, src_index] = 1
 
#weight = [[int(x) for x in input().split()] for i in range(n)]
start = get_valid_start_node(num_nodes)
end = get_valid_end_node(num_nodes)
inf = 1e8
visited = [False]*n # список из n элементов false, когда будем проверять станет True
dist = [inf]*n
dist[start] = 0 # элемент под индексом старт равен 0
 
def gofrom():
	index = 0
	distmin = inf
	for i in range(n):
		if dist[i] < distmin and visited[i]== False:
			distmin = dist[i]
			index = i
	return index
 
while False in visited:
    u = gofrom()
    for v in range(num_nodes):  # make sure to use num_nodes, not n unless it's defined
        if matrix[u, v] != 0 and not visited[v]:  # Access element directly with (u, v)
            dist[v] = min(dist[v], dist[u] + matrix[u, v])
    visited[u] = True
    count = 0
    for item in visited:
        if item == False:
            count += 1
    print(count)

print('Расстояние от', start + 1, "до", end + 1, 'равно', dist[end])