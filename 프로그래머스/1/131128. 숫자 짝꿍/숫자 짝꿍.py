def solution(X, Y):
    answer = ''
    num_list = []
    for i in range(10):
        x_count = X.count(str(i))
        y_count = Y.count(str(i))
        if x_count != 0 and y_count != 0:
            num_list.append(str(i)*min(x_count, y_count))
    num_list.sort(reverse=True)
    if not num_list:
        return "-1"
    for num in num_list:
        answer += num
    if all(char == "0" for char in answer):
        return "0"
    return answer