N = int(input())
meeting_list = []

for i in range(N):
    start, end = map(int, input().split())
    meeting_list.append([end, start])

meeting_list.sort()
time = 0
cnt = 0

for meeting in meeting_list:
    if time <= meeting[1]:
        cnt += 1
        time = meeting[0]

print(cnt)