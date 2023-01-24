from itertools import permutations

def solution(k, dungeons):
    answer = -1
    permu = list(permutations(dungeons, len(dungeons)))
    
    for p in permu:
        hp = k
        cnt = 0
        for i in p:
            if hp <= 0: 
                break
            if hp >= i[0]:
                hp -= i[1]
                cnt += 1
        if cnt > answer: 
            answer = cnt
        
    return answer