class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        self.top = Node(val, self.top)
        self.size += 1

    def pop(self):
        if self.top is None:
            return -1
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item

    def is_empty(self):
        if self.top is None:
            return 1
        else:
            return 0

    def is_top(self):
        if self.top is None:
            return -1
        else:
            return self.top.item

n = int(input())
stack = Stack()
print_list = []
while n > 0:
    order = input()
    if order.find(" ") != -1:
        order = order.split(" ")
        stack.push(int(order[1]))
    elif order == "pop":
        print_list.append(stack.pop())
    elif order == "size":
        print_list.append(stack.size)
    elif order == "top":
        print_list.append(stack.is_top())
    elif order == "empty":
        print_list.append(stack.is_empty())
    n -= 1
print(*print_list, sep="\n")
