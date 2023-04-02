equ = list(input().split('-'))
res = 0
for i in range(0, len(equ)):
    temp = list(map(int,equ[i].split('+')))
    if i == 0:
        res = sum(temp)
    else:
        res -= sum(temp)
        
print(res)