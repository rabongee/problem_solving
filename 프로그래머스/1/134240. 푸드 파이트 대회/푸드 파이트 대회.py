from collections import deque

def solution(food):
    answer = ''
    food_fight=deque([])
    food_fight.append('0')
    for i in range(len(food)-1,0,-1):
        for j in range(food[i]//2):
            food_fight.append(str(i))
            food_fight.appendleft(str(i))
    for fd in food_fight:
        answer += fd
    return answer