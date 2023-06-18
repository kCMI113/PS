import sys

def init(nums, tree, node, start, end):
    if start == end:
        # init leaf node
        tree[node] = [nums[start], nums[start]] # [min, max]
    else:
        # init child node first
        init(nums, tree, node*2, start, (start+end)//2)
        init(nums, tree, node*2+1, (start+end)//2+1, end)
        # then, init present node by using L,R child node
        tree[node] = [min(tree[node*2][0], tree[node*2+1][0]), max(tree[node*2][1], tree[node*2+1][1])]

def query(tree, node, start, end, left, right):
    # want to get total sum of [L,R] sub part

    if end < left or start > right:
        return [1e9+1, 0]
    elif left <= start and end <= right:
        return tree[node]
    
    L_res = query(tree, node*2, start, (start+end)//2, left, right)
    R_res = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return [min(L_res[0], R_res[0]), max(L_res[1], R_res[1])]
        
N, M = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
tree = [[1e9+1,0]]*(4*N)

# init tree
init(nums, tree, 1, 0, N-1)

for i in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    res = query(tree, 1, 0, N-1, num1-1, num2-1)
    print(res[0], end=" ")
    print(res[1])