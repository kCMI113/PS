import sys

N = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
cnt = 0

front, end = 0, N-1

while front<end:
    if nums[front]+nums[end] == x:
        cnt += 1
        end -= 1
    elif nums[front]+nums[end] < x:
        front += 1
    else:
        end -= 1

print(cnt)