import sys

N, M = map(int, sys.stdin.readline().split())
result = []
check = [False]*(N+1)


def recur(start, num):
    if num == M:
        print(' '.join(map(str, result)))
        return

    for i in range(start,N+1):
        if not check[i]:
            check[i] = True
            result.append(i)
            recur(i+1, num+1)
            check[i] = False
            result.pop()


recur(1, 0)