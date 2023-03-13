def my_bisect(num, _list):
    start = 0
    end = len(_list)-1
    
    while(start <= end):
        mid = (start+end)//2
        if num == _list[mid]:
            return 1
        elif num < _list[mid]:
            end = mid-1
        else:
            start = mid+1
    return 0
    
        
n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

for nums in m_list:
    print(my_bisect(nums, n_list))
        