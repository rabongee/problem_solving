import sys
from collections import deque, defaultdict


def dfs_recursive(node, visited):
    visited.append(node)
    graph[node].sort()
    for adjacent in graph[node]:
        if adjacent not in visited:
            dfs_recursive(adjacent, visited)
    return visited


def bfs_queue(start):
    visited = [start]
    q = deque([start])
    while q:
        node = q.popleft()
        graph[node].sort()
        for adjacent in graph[node]:
            if adjacent not in visited:
                q.append(adjacent)
                visited.append(adjacent)
    return visited


N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
print(' '.join(map(str, dfs_recursive(V, []))))
print(' '.join(map(str, bfs_queue(V))))