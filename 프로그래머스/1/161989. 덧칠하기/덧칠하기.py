def solution(n, m, section):
    answer = 0
    start = 0
    for i in section:
        if start <= i:
            answer += 1
            start = i+m
    return answer