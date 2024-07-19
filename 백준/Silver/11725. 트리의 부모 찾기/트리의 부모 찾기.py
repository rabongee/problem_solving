import sys
from collections import deque, defaultdict


def bfs_queue(g_dict, start):
    parent = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for child in g_dict[node]:
            if child not in parent:
                queue.append(child)
                parent[child] = node
    return parent


N = int(sys.stdin.readline())
graph = defaultdict(list)
for i in range(N-1):
    point1, point2 = map(int, sys.stdin.readline().split())
    graph[point1].append(point2)
    graph[point2].append(point1)

parent_nodes = bfs_queue(graph, 1)
for num in range(2, N+1):
    print(parent_nodes[num])