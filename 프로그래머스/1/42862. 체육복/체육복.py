def solution(n, lost, reserve):
    answer = 0
    student = {}
    for i in range(1,n+1):
        student[i] = 1
        if i in lost:
            student[i] -= 1
        if i in reserve:
            student[i] += 1
    for key in student.keys():
        if key != 1 or key != n:
            if student.get(key) > 1 and student.get(key-1) == 0:
                student[key] -= 1
                student[key - 1] += 1
            elif student.get(key) > 1 and student.get(key+1) == 0:
                student[key] -= 1
                student[key + 1] += 1
        elif key == 1:
            if student.get(key) > 1 and student.get(key + 1) == 0:
                student[key] -= 1
                student[key + 1] += 1
        elif key == n:
            if student.get(key) > 1 and student.get(key-1) == 0:
                student[key] -= 1
                student[key - 1] += 1
    for value in student.values():
        if value > 0:
            answer += 1
    return answer