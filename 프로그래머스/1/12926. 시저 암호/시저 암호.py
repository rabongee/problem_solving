def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += i
        elif i.isupper():
            answer += chr(ord(i) + n) if (ord(i) + n) <= ord('Z') else chr(ord(i) + n - 26)
        else:
            answer += chr(ord(i) + n) if (ord(i) + n) <= ord('z') else chr(ord(i) + n - 26)
    return answer