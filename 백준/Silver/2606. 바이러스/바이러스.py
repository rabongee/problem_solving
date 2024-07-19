import sys
from collections import deque, defaultdict


def bfs_queue(g_dict, start):
    visited = [start]
    queue = deque([start])
    count = 0
    while queue:
        node = queue.popleft()
        for virus in g_dict[node]:
            if virus not in visited:
                visited.append(virus)
                queue.append(virus)
                count += 1
    return count


computer = int(input())
com_connect = int(input())
network = defaultdict(list)
for _ in range(com_connect):
    com1, com2 = map(int, sys.stdin.readline().split())
    network[com1].append(com2)
    network[com2].append(com1)
print(bfs_queue(network, 1))