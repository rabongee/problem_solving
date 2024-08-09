from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    mandarin = defaultdict(int)
    for i in tangerine:
        mandarin[i] += 1
    box = sorted(mandarin.values())
    while k > 0:
        k -= box.pop()
        answer += 1
    return answer