def solution(n, left, right):
    answer = []
    for k in range(left, right+1):
        answer.append(max(k//n, k%n)+1)
    return answer
