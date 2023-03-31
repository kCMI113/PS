n = int(input())
times = list(map(int,input().split()))
times.sort()
res = [times[0]]

for i in range(1,len(times)):
    res.append(times[i] + res[-1])
    
print(sum(res))