def solution(arr):
    arr.sort(reverse=True)
    multi = arr[0]
    for i in range(1,len(arr)):
        num_1 = multi
        num_2 = arr[i]
        while True:
            divisor = num_1 % num_2
            if divisor == 0:
                multi = multi * arr[i] // num_2
                break
            num_1 = num_2
            num_2 = divisor
    return multi