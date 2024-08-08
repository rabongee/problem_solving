def solution(arr):
    answer = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        num_1 = answer
        num_2 = arr[i]
        while True:
            divisor = num_1 % num_2
            if divisor == 0:
                answer = answer * arr[i] // num_2
                break
            num_1 = num_2
            num_2 = divisor
    return answer