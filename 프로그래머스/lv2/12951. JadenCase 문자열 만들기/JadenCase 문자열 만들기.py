def solution(s):
    answer = ''
    str = s.split(' ')
    for S in str:
        answer += S.capitalize() +" "
    answer = answer[:len(answer)-1]
    return answer