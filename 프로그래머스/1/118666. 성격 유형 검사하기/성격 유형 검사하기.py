def solution(survey, choices):
    answer = ''
    mbti = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3}

    for sur, choice in zip(survey, choices):
        if choice < 4:
            mbti[sur[0]] += score[choice]
        else:
            mbti[sur[1]] += abs(score[choice])
    pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    for a, b in pairs:
        if mbti[a] < mbti[b]:
            answer += b
        else:
            answer += a
    return answer
