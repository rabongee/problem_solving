def solution(n):
    jump = [1,2]
    for i in range(2,n):
        jump.append(jump[i-1]+jump[i-2])
    if n == 1:
        return jump[0]
    else:
        return jump[-1] % 1234567