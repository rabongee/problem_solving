def solution(s):
    answer = ''
    s = s.title()
    num_str = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for i in range(len(s)):
        if i > 0 and s[i - 1] in num_str:
            answer += s[i].lower()
        else:
            answer += s[i]
    return answer