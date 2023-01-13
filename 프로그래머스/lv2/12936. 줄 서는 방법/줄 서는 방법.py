import itertools as itr
import math

def solution(n, k):
    answer = []
    nums = [i for i in range(1,n+1)]
    
    while nums:
        if(len(nums)<=5):
            answer += list(itr.permutations(nums))[k-1]
            break       
        else:
            fac = math.factorial(len(nums)-1)
            answer.append(nums[k//fac])
            nums.pop(k//fac)
            k %= fac
    
            
    return answer