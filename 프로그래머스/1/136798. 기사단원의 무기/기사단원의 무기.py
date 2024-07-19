def solution(number, limit, power):
    answer = 0
    Fe = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**(1/2))+1):
            if i % j == 0:
                count += 1
                if j < i//j:
                    count += 1
        Fe.append(count)
    for iron in Fe:
        if iron > limit:
            answer += power
        else:
            answer += iron
    return answer