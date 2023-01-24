def solution(n, lost, reserve):
    newres = set(reserve) - set(lost)
    newlos = set(lost) - set(reserve)
    newres = sorted(newres)
    for R in newres:
        if R-1 in newlos:
            newlos.remove(R-1)
        elif R+1 in newlos:
            newlos.remove(R+1)
    answer = n - len(newlos)
    return answer