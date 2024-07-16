from collections import deque

testcase = int(input())

for _ in range(testcase):
    count = 0
    document, position = map(int, input().split(" "))
    ranks = list(map(int,input().split(" ")))
    print_queue = deque()
    for i, rank in enumerate(ranks):
        d = {
            "index": i,
            "rank": rank,
        }
        print_queue.append(d)
    while print_queue:
        first = print_queue.popleft() # 0, 1
        for queue in print_queue: # 1, 2
            if first["rank"] < queue["rank"]:
                print_queue.append(first)
                break
        if first in print_queue:
            continue
        count += 1
        if first["index"] == position:
            print(count)
            break