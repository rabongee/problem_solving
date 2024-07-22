def solution(s):
    answer = 0
    str_num = ''
    str_dict = []
    x = s[0]
    for i in range(len(s)):
        str_num += s[i]
        if str_num.count(x) == len(str_num)-str_num.count(x):
            str_dict.append(str_num)
            str_num = ''
            if i < len(s)-1:
                x = s[i+1]
    if len(str_num) != 0:
        answer += 1
    answer += len(str_dict)
    return answer