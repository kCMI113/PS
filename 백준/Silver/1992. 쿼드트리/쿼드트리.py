size = int(input())
data = [list(input()) for _ in range(size)]
res = []

def divide_matrix(row:int, col:int, size:int) -> None:
    all_one = True
    all_zero = True

    for j in range(col, col+size):
        for i in range(row, row+size):
            if data[i][j] != '0':
                all_zero = False
            if data[i][j] != '1':
                all_one = False
                
    if all_zero:
        res.append('0')
        return
    elif all_one:
        res.append('1')
        return
    
    res.append('(')
    divide_matrix(row,        col,        size//2)
    divide_matrix(row,        col+size//2, size//2)
    divide_matrix(row+size//2, col,        size//2)
    divide_matrix(row+size//2, col+size//2, size//2)
    res.append(')')


divide_matrix(0, 0, size)
print(''.join(res))