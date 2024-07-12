from collections import deque

def queue(num):
    cards = deque([i for i in range(1, num+1)])
    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    return cards.popleft()

n = int(input())
print(queue(n))