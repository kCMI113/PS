def solution(array, commands):
    answer = []
    n = len(array)
    for C in commands:
        i,j,k = C[0]-1, C[1], C[2]-1
        temp = array[i:j]
        temp.sort()
        answer.append(temp[k])
        
    return answer