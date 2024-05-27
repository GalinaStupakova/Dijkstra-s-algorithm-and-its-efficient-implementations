import timeit 
code_to_test = '''
n = 12
weight = [[0, 17, 0, 39, 0, 0, 0, 0, 0, 0, 0, 0], [17, 0, 1, 0, 16, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [39, 0, 0, 0, 42, 0, 0, 0, 2, 0, 0, 0], [0, 16, 0, 42, 0, 26, 13, 11, 0, 0, 0, 0], [0, 0, 0, 0, 26, 0, 50, 0, 0, 0, 0, 0], [0, 0, 0, 0, 13, 50, 0, 22, 0, 0, 22, 0], [0, 0, 0, 0, 11, 0, 22, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0, 0, 9, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 22, 0], [0, 0, 0, 0, 0, 0, 22, 0, 0, 22, 0, 27], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0]]
start = 0
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
	for v in range(n):
		if weight[u][v] !=0 and (not visited[v]):
			dist[v] = min(dist[v], dist[u]+weight[u][v])
	visited[u]=True
for i in range(len(dist)):
	print('Расстояние от', start + 1, "до", i +1, 'равно', dist[i]) '''
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
