def solution(n):
    fibo = []
    for i in range(0,n+1):
        if i<2:
            fibo.append(i)
        else:
            fibo.append(fibo[i-1]%1234567 + fibo[i-2]%1234567)
            
    answer = fibo[n]%1234567
    return answer