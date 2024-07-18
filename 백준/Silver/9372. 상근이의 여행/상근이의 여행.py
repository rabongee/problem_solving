import sys
from collections import defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    is_visited = defaultdict(bool)
    dfs_stack = [1]
    count = 0
    while dfs_stack:
        top = dfs_stack.pop()
        is_visited[top] = True
        next_countries = graph[top]
        for country in next_countries:
            if not is_visited[country] and country not in dfs_stack:
                dfs_stack.append(country)
                count += 1

    print(count)