import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
result = []
for i in range(1, N+1):
    result.append(i)
nPr = itertools.permutations(result, M)
for perm in nPr:
    print(" ".join(map(str, perm)))