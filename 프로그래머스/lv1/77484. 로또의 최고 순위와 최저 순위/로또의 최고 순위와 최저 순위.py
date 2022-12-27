def solution(lottos, win_nums):
    answer = []
    zeros = lottos.count(0)
    cnt=0
    for num in lottos:
        if win_nums.count(num) >0:
            cnt +=1
    for i in range(1,3):
        if cnt == 6:
            answer.append(1)
        elif cnt == 5:
            answer.append(2)
        elif cnt == 4:
            answer.append(3)
        elif cnt == 3:
            answer.append(4)
        elif cnt == 2:
            answer.append(5)
        else:
            answer.append(6)
        cnt+=zeros
    answer.sort()
        
    return answer