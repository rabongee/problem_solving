from collections import deque

def solution(d, p, r):
    count = 0
    print_queue = deque()
    for i, rank in enumerate(r):
        paper = {
            "index": i,
            "rank": rank,
        }
        print_queue.append(paper)
    while print_queue:
        first = print_queue.popleft()
        for queue in print_queue:
            if first["rank"] < queue["rank"]:
                print_queue.append(first)
                break
        if first in print_queue:
            continue
        count += 1
        if first["index"] == p:
            print(count)
            break


testcase = int(input())
for _ in range(testcase):
    document, position = map(int, input().split(" "))
    ranks = list(map(int,input().split(" ")))
    solution(document, position, ranks)