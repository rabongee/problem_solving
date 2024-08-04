def solution(s):
    zero_count = 0
    trans = 0
    while s != '1':
        zero_count += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        trans += 1
    return [trans, zero_count]