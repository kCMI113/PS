def solution(s):
    answer = True
    cnt = 0
    
    if(s[0] == ')' or s[-1] == '('):
        answer = False
    else:
        for c in s:
            if c == '(':
                cnt += 1
            elif cnt>0 :
                cnt -= 1
        answer = (cnt == 0)

    return answer