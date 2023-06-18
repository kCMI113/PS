import sys

def init(nums, tree, node, start, end, oper):
    if start == end:
        # init leaf node
        tree[node] = nums[start]
    else:
        # init child node first
        init(nums, tree, node*2, start, (start+end)//2, oper)
        init(nums, tree, node*2+1, (start+end)//2+1, end, oper)
        # then, init present node by using L,R child node
        tree[node] = oper(tree[node*2], tree[node*2+1])

def query(tree, node, start, end, left, right, oper):
    # want to get total sum of [L,R] sub part

    if end < left or start > right:
        return -1
    elif left <= start and end <= right:
        return tree[node]
    
    L_res = query(tree, node*2, start, (start+end)//2, left, right, oper)
    R_res = query(tree, node*2+1, (start+end)//2+1, end, left, right, oper)
    if L_res < 0:
        return R_res
    if R_res < 0:
        return L_res
    
    return oper(R_res, L_res)

        
N, M = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
min_tree = [-1]*(4*N)
max_tree = [-1]*(4*N)

# init tree
init(nums, min_tree, 1, 0, N-1, min)
init(nums, max_tree, 1, 0, N-1, max)


for i in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())

    print(query(min_tree, 1, 0, N-1, num1-1, num2-1, min), end=" ")
    print(query(max_tree, 1, 0, N-1, num1-1, num2-1, max))