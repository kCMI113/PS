# https://www.acmicpc.net/problem/2630
import sys

N = int(sys.stdin.readline().rstrip())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
blue = 0
white = 0


def devide(row, col, step):
    global blue, white

    flag = table[row][col]
    for i in range(row, row + step):
        for j in range(col, col + step):
            if table[i][j] != flag:
                devide(row, col, step // 2)  # 좌상
                devide(row + step // 2, col, step // 2)  # 좌하
                devide(row, col + step // 2, step // 2)  # 우상
                devide(row + step // 2, col + step // 2, step // 2)  # 우하
                return
    if flag:
        blue += 1
        return
    white += 1


devide(0, 0, N)
print(white, blue, sep="\n")