from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    declare = defaultdict(set)
    stop = defaultdict(int)
    for r in report:
        declarer, target = r.split()
        if target not in declare[declarer]:
            declare[declarer].add(target)
            stop[target] += 1

    for user in id_list:
        count = 0
        for tar in declare[user]:
            if stop[tar] >= k:
                count += 1
        answer.append(count)
    return answer