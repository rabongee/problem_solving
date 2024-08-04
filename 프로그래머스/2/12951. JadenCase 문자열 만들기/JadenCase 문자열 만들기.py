def solution(s):
    answer = ''
    s = s.title()
    s_list = list(s)
    num_str = {'0','1','2','3','4','5','6','7','8','9'}
    for i in range(len(s_list)-1):
        if s_list[i] in num_str:
            s_list[i+1] = s_list[i+1].lower()
        answer += s_list[i]
    answer += s_list[-1]
    return answer