def solution(elements):
    answer = set()
    for _ in range(len(elements)):
        for i in range(1, len(elements)+1):
            answer.add(sum(elements[0:0 + i]))
        elements = elements[1:] + elements[0:1]
    return len(answer)