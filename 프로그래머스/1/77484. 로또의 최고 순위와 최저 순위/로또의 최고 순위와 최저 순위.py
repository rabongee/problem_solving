def solution(lottos, win_nums):
    answer = []
    max_count = 0
    min_count = 0
    rank = [6,6,5,4,3,2,1]
    for num in lottos:
        if num in win_nums:
            min_count +=1
        elif num == 0:
            max_count +=1
    max_count += min_count
    answer.append(rank[max_count])
    answer.append(rank[min_count])
    return answer