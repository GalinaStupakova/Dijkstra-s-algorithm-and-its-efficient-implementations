import heapq

n = int(input())
weight = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
start = int(input()) - 1
inf = 1e8
visited = [False]*n
dist = [inf]*n
dist[start] = 0

# Create a binary heap (min-heap) to store the vertices that have not yet been included in the shortest path tree
vertex_heap = [(0, start)]

# Build the adjacency list of the graph
for i in range(n):
    for j in range(n):
        if weight[i][j] != 0:
            graph[i].append((j, weight[i][j]))

# Loop until the vertex heap is empty
while vertex_heap:
    # Extract the vertex with the smallest distance from the heap
    current_distance, current_vertex = heapq.heappop(vertex_heap)

    # Skip the vertex if it has already been included in the shortest path tree
    if current_distance > dist[current_vertex]:
        continue

    # Update the distance to each neighboring vertex
    for neighbor, weight in graph[current_vertex]:
        if not visited[neighbor]:
            distance = current_distance + weight

            # Update the distance if it is smaller than the current distance
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(vertex_heap, (distance, neighbor))

    visited[current_vertex] = True

for i in range(len(dist)):
    print('Расстояние от', start + 1, "до", i +1, 'равно', dist[i])