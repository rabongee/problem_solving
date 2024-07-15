def solution(d, p, r):
    count = 0
    i = 0
    while True:
        if max(r) == r[i]:
            count += 1
            r[i] = 0
            if i == p:
                break
        i += 1
        if i == d:
            i = 0
    return count

n = int(input())
answer_list = []
for i in range(n):
    document, position = map(int, input().split(" "))
    rank = input().split(" ")
    rank = list(map(int, rank))
    answer_list.append(solution(document, position, rank))
print('\n'.join(map(str, answer_list)))