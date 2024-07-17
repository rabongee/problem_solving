def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        box = []
        for _ in range(m):
            box.append(score.pop())
        answer += min(box) * m
    return answer