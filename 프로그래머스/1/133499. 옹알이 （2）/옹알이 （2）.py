def solution(babbling):
    answer = 0
    babies = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for baby in babies:
            if baby in bab and (baby*2) not in bab:
                bab = bab.replace(baby, '*')
        if all(char == '*' for char in bab):
            answer += 1
    return answer