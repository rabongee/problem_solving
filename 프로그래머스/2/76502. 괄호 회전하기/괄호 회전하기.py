from collections import deque


def solution(s):
    answer = 0
    bracket = deque(s)
    br_dict = {")": "(", "}": "{", "]": "["}
    open_bracket = "({["
    for _ in range(len(s)):
        bool_val = True
        br_list = []
        for br in bracket:
            if br in open_bracket:
                br_list.append(br)
            else:
                if not br_list:
                    bool_val = False
                    break
                elif br_list.pop() != br_dict[br]:
                    bool_val = False
                    break
        if bool_val and len(br_list) == 0:
            answer += 1
        bracket.append(bracket.popleft())
    return answer