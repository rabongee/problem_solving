def solution(brown, yellow):
    answer = []
    combination = []
    total = brown + yellow
    for height in range(1,int(total**0.5)+1):
        if total % height == 0:
            width = total//height
            combination.append((width, height))
    for w, h in combination:
        if (w-2)*(h-2) == yellow:
            answer.append(w)
            answer.append(h)
            break
    return answer