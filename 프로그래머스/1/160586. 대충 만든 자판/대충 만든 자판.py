from collections import defaultdict

def solution(keymap, targets):
    answer = []
    key_num = defaultdict(list)
    for key in keymap:
         for i in range(len(key)):
             key_num[i].append(key[i])
    for target in targets:
        count = 0
        for i in range(len(target)):
            check_num = check(key_num,target[i])
            if check_num == -1:
                count = -1
                break
            else:
                count += check_num
        answer.append(count)
    return answer

def check(key_num, tar):
    for idx in key_num.keys():
        if tar in key_num[idx]:
            return idx+1
    return -1