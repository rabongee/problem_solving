import sys
import heapq

n = int(input())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)