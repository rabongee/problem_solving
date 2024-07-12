new_list = []
while True:
    a, b = input().split(' ')
    a, b = int(a), int(b)
    if a+b == 0:
        break
    else:
        new_list.append(a+b)
for i in new_list:
    print(i)