import sys
from collections import deque

d = ((-1, 0), (1, 0), (0, -1), (0, 1))
def search(row, col):
    q = deque([(row, col, 1)])
    maze[row][col] = 0
    while q:
        r, c, opr = q.popleft()
        if r == N-1 and c == M-1:
            return opr

        for row_add, col_add in d:
            next_r = r + row_add
            next_c = c + col_add
            if 0 <= next_r < N and 0 <= next_c < M and maze[next_r][next_c] == 1:
                q.append((next_r, next_c, opr+1))
                maze[next_r][next_c] = 0



N, M = map(int, sys.stdin.readline().split()) #N이 세로 M은 가로
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
print(search(0, 0))