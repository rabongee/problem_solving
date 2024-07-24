import sys


def cabbage_dfs_stack(graph):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    rows, cols = len(graph), len(graph[0])
    cnt = 0
    for row in range(rows):
        for col in range(cols):
            if graph[row][col] != 1:
                continue
            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                graph[x][y] = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx<0 or nx >= rows or ny < 0 or ny >= cols or graph[nx][ny] != 1:
                        continue
                    stack.append((nx, ny))
    return cnt


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] = 1
    print(cabbage_dfs_stack(graph))