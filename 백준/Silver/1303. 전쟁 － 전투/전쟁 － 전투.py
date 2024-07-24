import sys
from collections import deque

d = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(r, c, soldier_type):
    q = deque([])
    q.append((r, c))
    my_matrix[r][c] = 'N'
    count = 1
    while q:
        r, c = q.popleft()
        for row_add, col_add in d:
            next_r = r + row_add
            next_c = c + col_add
            if 0 <= next_r < M and 0 <= next_c < N and my_matrix[next_r][next_c] == soldier_type:
                q.append((next_r, next_c))
                my_matrix[next_r][next_c] = 'N'
                count += 1
    return count**2


N, M = map(int, sys.stdin.readline().split())
my_matrix = [list(sys.stdin.readline().strip()) for _ in range(M)]
w_count = 0
b_count = 0


for row in range(M):
    for col in range(N):
        if my_matrix[row][col] == 'W':
            w_count += bfs(row, col, 'W')
        elif my_matrix[row][col] == 'B':
            b_count += bfs(row, col, 'B')

print(w_count, b_count)