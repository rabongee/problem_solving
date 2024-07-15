def solution(a, b):
    day = 0
    month = {1: 31, 2:29, 3:31, 4:30, 5:31, 6:30,
             7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    week = {0:'FRI', 1:'SAT', 2:'SUN', 3:'MON',
            4:'TUE', 5:'WED', 6:'THU',}
    for i in range(1,a):
        day += month[i]
    day += b-1
    answer = week[day % 7]
    return answer