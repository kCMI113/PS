r = 31
M = 1234567891
N = int(input())
string = list(input())
res = 0

for i in range(N):
    num = ord(string[i]) - ord("a") + 1
    num = num * (r**i) % M
    res += num
    
print(res)