from collections import defaultdict
def dfs(graph, start, visited, path):
    visited[start] = True
    path.append(start)
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited, path)
graph = defaultdict(list)
n, e = map(int, input().split())
for _ in range(e):
    u, v = input().split()
    graph[u].append(v)
if '0' in graph:
    start = '0'
else:
    start = 'A'
visited = defaultdict(bool)
path = []
dfs(graph, start, visited, path)
print(path)
