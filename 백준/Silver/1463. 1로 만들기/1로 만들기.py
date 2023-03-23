n = int(input())

res = [0 for i in range(n+1)]

for i in range(2, n+1):
    cnt = res[i-1]+1 #1을 빼는 경우
    if i%2==0:
        cnt = min(cnt, res[i//2]+1) #2의 배수인 경우
    if i%3==0:
        cnt = min(cnt, res[i//3]+1) #3의 배수인 경우
    res[i] = cnt #모든 경우의 수 중에서 가장 연산 횟수가 작은 것을 선택

print(res[n])

