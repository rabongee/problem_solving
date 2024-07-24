import sys
from collections import deque

def bfs_queue(A, B):
    queue = deque([(A,1)])
    visited = set([A])

    while queue:
        cur, opr = queue.popleft()
        if cur == B:
            return opr

        next_num = cur *2
        if next_num not in visited and next_num <= B:
            queue.append((next_num,opr+1))
            visited.add(next_num)

        next_num = cur * 10 +1
        if next_num not in visited and next_num <= B:
            queue.append((next_num,opr+1))
            visited.add(next_num)
    return -1

A, B = map(int, sys.stdin.readline().split())
print(bfs_queue(A, B))