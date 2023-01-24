def solution(n, lost, reserve):
    answer = 0
    for R in range(n+1):
        if R in lost and R in reserve:
            lost.remove(R)
            reserve.remove(R)
    reserve.sort()
    lost.sort()
    for R in reserve:
        if R-1 in lost:
            lost.remove(R-1)
        elif R+1 in lost:
            lost.remove(R+1)
    answer = n - len(lost)
    return answer