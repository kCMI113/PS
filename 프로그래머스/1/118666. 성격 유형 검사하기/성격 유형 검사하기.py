def solution(survey, choices):
    answer = ''
    types = ["R","T","C","F","J","M","A","N"]
    type_list = {k:v for v, k in enumerate(types)}
    score_list = [v for v in range(3,0,-1)]
    type_score = [0 for _ in range(8)]
    
    for s, c in zip(survey,choices):
        if c == 4:
            continue
        if c < 4:
            type_score[type_list[s[0]]] += score_list[c-1]
        if c > 4:
            type_score[type_list[s[1]]] += score_list[7-c]
            
    for i in range(1,len(type_score),2):
        answer += types[i-1] if type_score[i-1] >= type_score[i] else types[i]
    
    return answer