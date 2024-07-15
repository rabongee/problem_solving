from collections import deque

def solution(n):
    cards = deque([i for i in range(1, n+1)])
    while n > 1:
        print(cards.popleft(), end=' ')
        cards.append(cards.popleft())
        n -= 1
    return cards.popleft()

n = int(input())
print(solution(n))