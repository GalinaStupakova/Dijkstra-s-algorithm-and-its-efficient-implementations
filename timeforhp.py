import timeit 
code_to_test = '''
import heapq

n = 12
weight = [[0, 17, 0, 39, 0, 0, 0, 0, 0, 0, 0, 0], [17, 0, 1, 0, 16, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [39, 0, 0, 0, 42, 0, 0, 0, 2, 0, 0, 0], [0, 16, 0, 42, 0, 26, 13, 11, 0, 0, 0, 0], [0, 0, 0, 0, 26, 0, 50, 0, 0, 0, 0, 0], [0, 0, 0, 0, 13, 50, 0, 22, 0, 0, 22, 0], [0, 0, 0, 0, 11, 0, 22, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0, 0, 9, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 22, 0], [0, 0, 0, 0, 0, 0, 22, 0, 0, 22, 0, 27], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0]]
graph = [[] for _ in range(n)]
start = 0
inf = 1e8
visited = [False]*n
dist = [inf]*n
dist[start] = 0


vertex_heap = [(0, start)]

for i in range(n):
    for j in range(n):
        if weight[i][j] != 0:
            graph[i].append((j, weight[i][j]))


while vertex_heap:
    # Extract the vertex with the smallest distance from the heap
    current_distance, current_vertex = heapq.heappop(vertex_heap)

    if current_distance > dist[current_vertex]:
        continue

    for neighbor, weight in graph[current_vertex]:
        if not visited[neighbor]:
            distance = current_distance + weight

            # Update the distance if it is smaller than the current distance
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(vertex_heap, (distance, neighbor))

    visited[current_vertex] = True

for i in range(len(dist)):
    print('Расстояние от', start + 1, "до", i +1, 'равно', dist[i]) '''
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
