import sys

n = int(sys.stdin.readline())
nums = [0]
out = []
res = []
itr = nums[-1]+1

for i in range(n):
    res.append(int(sys.stdin.readline()))

res = list(reversed(res))

while res:
    query = res.pop()
    if nums[-1] < query:
        for i in range(itr,query+1):
            nums.append(i)
            out.append('+')
        itr = nums[-1]+1

    if nums[-1] >= query:
        out.append('-')
        nums.pop()
    else:
        out.append('NO')
        break
    
if 'NO' in out:
    print('NO')
else:
    for r in out:
        print(r)
