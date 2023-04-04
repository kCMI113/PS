import sys

k, n = map(int, input().split())
cable = []

for i in range(k):
    cable.append(int(sys.stdin.readline()))

start, end = 1,max(cable)
new_n = 0
max_len = 0

while(start<=end):
    mid = (start+end)//2
    #new_n = sum(map(lambda num:num//mid, cable))
    new_n = sum([num//mid for num in cable])
    if new_n >= n:
        max_len = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(max_len)