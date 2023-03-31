n = int(input())
res = []

for i in range(n):
    total = list(input())
    brack = [total[0]]
    for i in range(1,len(total)): 
        if brack and brack[-1] == '(' and total[i] == ')':
            brack.pop()
        else:
            brack.append(total[i]) 
    if brack:
        res.append("NO")
    else:
        res.append("YES")
        
for r in res:
    print(r)