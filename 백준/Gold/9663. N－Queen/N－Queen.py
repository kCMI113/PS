import sys

def find_q(row:int, N:int) -> int:
    if row == N:
        global res
        res += 1
        return
    
    for i in range(N):
        # exist
        if check[i]:
            continue
        
        board[row] = i
        
        flag = 1
        for j in range(row):
            # same col or diag
            if board[row] == board[j] or row - j == abs(board[row]- board[j]):
                flag = 0
                break
        
        if flag:
            find_q(row+1, N)
            check[i] = 0

N = int(input())
check = [0 for _ in range(N)]
board = [-1 for _ in range(N)]
res = 0

find_q(0, N)

print(res)