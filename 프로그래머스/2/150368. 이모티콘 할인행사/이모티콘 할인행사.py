from itertools import product

def emotORplus(threshold_rate, threshold_cost, emot_cost, discount):
    user_buy = sum([emot_cost[i] if discount[i] >= threshold_rate else 0 for i in range(len(discount))])
    if user_buy >= threshold_cost:
        return 1,0
    return 0,user_buy

def solution(users, emoticons):
    answer = [0,0]
    discount_rate = [i for i in range(10,50,10)]
    
    for disc_rate in product(discount_rate, repeat=len(emoticons)):
        case_res = [0,0]
        new_emot_cost = [emoticons[i] - (disc_rate[i]/100)*emoticons[i] for i in range(len(emoticons))]
        
        for u in users:
            user_res = emotORplus(u[0], u[1], new_emot_cost, list(disc_rate))
            case_res[0] += user_res[0]
            case_res[1] += user_res[1]
        
        if case_res[0] < answer[0]:
            continue
        if case_res[0] > answer[0]:
            answer = case_res
        if case_res[0] == answer[0] and case_res[1]>=answer[1]:
            answer = case_res
        
        
    return answer