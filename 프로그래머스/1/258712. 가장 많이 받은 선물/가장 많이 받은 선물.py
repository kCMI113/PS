def solution(friends, gifts):
    friend_dict = {v:k for k,v in enumerate(friends)}
    gift_list = [[0 for _ in range(len(friend_dict))] for _ in range(len(friend_dict))]
    gift_point = [0 for _ in range(len(friend_dict))]
    next_gift = [0 for _ in range(len(friend_dict))]
    
    for gift in gifts:
        A, B = gift.split(" ")
        A, B = friend_dict[A], friend_dict[B]
        gift_list[A][B] += 1
    
    for row in range(len(friend_dict)):
        fst = sum(gift_list[row])
        snd = sum(data[row] for data in gift_list)
        gift_point[row] = fst-snd
        
    for row in range(len(friend_dict)):
        for col in range(row+1, len(friend_dict)):
            if gift_list[row][col] > gift_list[col][row]: # case1
                next_gift[row] += 1
                
            if gift_list[row][col] < gift_list[col][row]: # case1
                next_gift[col] += 1
                
            if gift_list[row][col] == gift_list[col][row]: # case2
                if gift_point[row] > gift_point[col]:
                    next_gift[row] += 1
                if gift_point[row] < gift_point[col]:
                    next_gift[col] += 1
        
    return max(next_gift)