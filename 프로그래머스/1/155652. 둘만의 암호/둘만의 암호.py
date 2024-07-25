import string

def solution(s, skip, index):
    answer = ''
    alpha = list(string.ascii_lowercase)
    for sk in skip:
        alpha.remove(sk)
    for c in s:
        num = alpha.index(c)+index
        if num >= len(alpha):
            num = num % len(alpha)
        answer += alpha[num]
    return answer