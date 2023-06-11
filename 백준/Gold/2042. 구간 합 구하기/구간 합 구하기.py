import sys

def init(nums, tree, node, start, end):
    if start == end:
        # init leaf node
        tree[node] = nums[start]
        idx_node[start] = node
    else:
        # init child node first
        init(nums, tree, node*2, start, (start+end)//2)
        init(nums, tree, node*2+1, (start+end)//2+1, end)
        # then, init present node by using L,R child node
        tree[node] = tree[node*2] + tree[node*2+1]

def query(tree, node, start, end, left, right):
    # want to get total sum of [L,R] sub part

    if end < left or start > right:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    
    L_sum = query(tree, node*2, start, (start+end)//2, left, right)
    R_sum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return L_sum+R_sum

def update(nums, tree, idx, val): 
    # bottom-up search

    diff = val - nums[idx] 
    nums[idx] = val
    node = idx_node[idx]

    while node:
        tree[node] += diff
        node //= 2
        

N, M, K = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0]*(4*N)
idx_node = [0]*N

# init tree
init(nums, tree, 1, 0, N-1)

for i in range(M+K):
    q, num1, num2 = map(int, sys.stdin.readline().split())

    if q == 1:
        update(nums, tree, num1-1, num2)
    else:
        print(query(tree, 1, 0, N-1, num1-1, num2-1))