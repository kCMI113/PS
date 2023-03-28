T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    res = [[i for i in range(1,n+1)]]
    
    for j in range(1,k+1):
        res.append([res[j-1][0]])
        for l in range(1,n):
            res[j].append(sum(res[j-1][:l+1]))
            
    print(res[k][n-1])