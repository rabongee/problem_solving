from collections import defaultdict


def solution(keymap, targets):
    key_num = defaultdict(int)
    for key in keymap:
        for i, char in enumerate(key):
            if key_num[char] == 0 or key_num[char] > i + 1:
                key_num[char] = i + 1

    answer = []
    for target in targets:
        count = 0
        for char in target:
            if key_num[char] == 0:
                count = -1
                break
            count += key_num[char]
        answer.append(count)
    return answer