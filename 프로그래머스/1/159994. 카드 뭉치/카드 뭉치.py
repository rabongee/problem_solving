from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    for i in range(len(goal)):
        target = goal.popleft()
        if target in cards1:
            if target != cards1.popleft():
                answer = "No"
        elif target in cards2:
            if target != cards2.popleft():
                answer = "No"
    return answer