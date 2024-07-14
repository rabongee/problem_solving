def solution(k, score):
    answer = []
    hall_of_fame = []
    for i in range(len(score)):
        if i < k:
            hall_of_fame.append(score[i])
        else:
            hall_of_fame[k-1] = max(hall_of_fame[k-1], score[i])
        hall_of_fame.sort(reverse=True)
        answer.append(min(hall_of_fame))
    return answer