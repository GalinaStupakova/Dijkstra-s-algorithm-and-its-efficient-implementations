import snap
import heapq
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

# Create a binary heap (min-heap) to store the vertices that have not yet been included in the shortest path tree
vertex_heap = [(0, start)]

# Loop until the vertex heap is empty
while vertex_heap:
    # Extract the vertex with the smallest distance from the heap
    current_distance, current_vertex = heapq.heappop(vertex_heap)

    # Skip the vertex if it has already been included in the shortest path tree
    if current_distance > dist[current_vertex]:
        continue

    # Update the distance to each neighboring vertex
    for neighbor in range(num_nodes):
        if matrix[current_vertex, neighbor] != 0 and not visited[neighbor]:
            distance = current_distance + matrix[current_vertex, neighbor]

            # Update the distance if it is smaller than the current distance
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(vertex_heap, (distance, neighbor))

    visited[current_vertex] = True
    count = 0
    for item in visited:
        if item == False:
            count += 1
    print(count)

print('Расстояние от', start + 1, "до", end + 1, 'равно', dist[end])