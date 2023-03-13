n,m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
start, end = 0, trees[-1]

while(start<=end):
    mid = (start+end)//2
    total_len = 0
    
    for i in trees:
        if (i>mid):
            total_len += (i-mid)
    
    if total_len >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(res)
    