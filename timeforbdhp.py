import timeit 
code_to_test = '''
import snap
import heapq
from scipy.sparse import lil_matrix
 
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
start = 549
end = 2999
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

print('Расстояние от', start + 1, "до", end + 1, 'равно', dist[end])'''
elapsed_time = timeit.timeit(code_to_test, number=10)/10
print(elapsed_time)