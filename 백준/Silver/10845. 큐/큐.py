import sys

input = sys.stdin.readline


class queue:
    def __init__(self) -> None:
        self.size = 0
        self.item = []

    def push(self, x):
        self.item.append(x)

    def pop(self):
        if self.empty():
            print(-1)
        else:
            print(self.item.pop(0))

    def get_size(self):
        print(len(self.item))

    def empty(self):
        if not self.item:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            print(-1)
        else:
            print(self.item[0])

    def back(self):
        if self.empty():
            print(-1)
        else:
            print(self.item[-1])


que = queue()
n = int(input())

for _ in range(n):
    ele = list(input().split())
    match ele[0]:
        case "push":
            que.push(int(ele[1]))
        case "front":
            que.front()
        case "back":
            que.back()
        case "size":
            que.get_size()
        case "pop":
            que.pop()
        case "empty":
            print(que.empty())
