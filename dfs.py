

'''Depth First Search uses STACK AND RECURSION
'''
#import defaultdict
from collections import defaultdict
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
         if not visited[neighbour]:
            path = dfs(graph, neighbour, visited, path)
    return path
graph=defaultdict(list)
n,e=map(int,input().split())
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
#print(graph)
start='A'
visited=defaultdict(bool)
 #type ur code here
traversedpath=dfs(graph,start,visited,path)
print(traversedpath)
