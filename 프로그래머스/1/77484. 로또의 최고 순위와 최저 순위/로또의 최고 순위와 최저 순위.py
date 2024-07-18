def solution(lottos, win_nums):
    answer = []
    win_dict = {}
    rank = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    max_count = 0
    min_count = 0
    for num in win_nums:
        win_dict[num] = True
    for lotto in lottos:
        if win_dict.get(lotto):
            min_count += 1
        elif lotto == 0:
            max_count += 1
    max_count += min_count
    answer.append(rank.get(max_count))
    answer.append(rank.get(min_count))
    return answer