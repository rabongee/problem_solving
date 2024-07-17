import sys


def percolate_down(arr, cur):
    smallest = cur
    left = 2 * cur
    right = 2 * cur + 1

    if left <= len(arr) - 1 and arr[left] < arr[smallest]:
        smallest = left

    if right <= len(arr) - 1 and arr[right] < arr[smallest]:
        smallest = right

    if smallest != cur:
        arr[cur], arr[smallest] = arr[smallest], arr[cur]
        percolate_down(arr, smallest)


n = int(input())
arr = [None]
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(arr)-1 < 1:
            print(0)
        else:
            arr[1], arr[-1] = arr[-1], arr[1]
            print(arr.pop())
            percolate_down(arr,1)

    else:
        arr.append(x)
        cur = len(arr) - 1
        parent = cur // 2
        while parent > 0:
            if arr[cur] < arr[parent]:
                arr[parent], arr[cur] = arr[cur], arr[parent]
            cur = parent
            parent = cur // 2