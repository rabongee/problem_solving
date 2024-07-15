def solution(n):
    answer = ''
    reverse_num = list(str(n))
    reverse_num.sort(reverse=True)
    for num in reverse_num:
        answer = answer + num
    return int(answer)