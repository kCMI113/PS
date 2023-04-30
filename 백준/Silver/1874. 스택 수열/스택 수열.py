import sys
import heapq

n = int(sys.stdin.readline())
nums = [0]
res = []
out = []
itr = nums[-1]+1

for i in range(n):
    out.append(int(sys.stdin.readline()))

out = list(reversed(out))

while out:
    query = out.pop()
    if nums[-1] < query:
        for i in range(itr,query+1):
            nums.append(i)
            res.append('+')
        itr = nums[-1]+1

    if nums[-1] == query:
        res.append('-')
        nums.pop()
    else:
        res.append('NO')
        break
if 'NO' in res:
    print('NO')
else:
    for r in res:
        print(r)