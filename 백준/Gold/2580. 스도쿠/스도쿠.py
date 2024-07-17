import sys

input = sys.stdin.readline
N = 9

pan = [list(map(int, input().split())) for _ in range(N)]
zeros = []
n_zeros = 0
for x in range(N):
    for y in range(N):
        if not pan[x][y]:
            zeros.append([x, y])
            n_zeros += 1


def check_row(x, num):
    for i in range(N):
        if pan[x][i] == num:
            return False
    return True


def check_col(y, num):
    for i in range(N):
        if pan[i][y] == num:
            return False
    return True


def check_square(x, y, num):
    new_x = (x // 3) * 3
    new_y = (y // 3) * 3

    for i in range(new_x, new_x + 3):
        for j in range(new_y, new_y + 3):
            if pan[i][j] == num:
                return False
    return True


def sdoku(depth):
    if depth == n_zeros:
        for line in pan:
            print(*line)
        exit(0)

    x, y = zeros[depth]
    for num in range(1, 10):
        if check_row(x, num) and check_col(y, num) and check_square(x, y, num):
            pan[x][y] = num
            sdoku(depth + 1)
            pan[x][y] = 0


sdoku(0)
