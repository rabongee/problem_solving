def solution(arr):
    arr.remove(min(arr))
    answer = arr
    if not answer:
        answer.append(-1)
    return answer