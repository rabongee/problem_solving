def solution(s):
    answer = []
    word_dict={}
    for idx, word in enumerate(s):
        answer.append(-1) if word not in word_dict else answer.append(idx-word_dict[word])
        word_dict[word] = idx
    return answer