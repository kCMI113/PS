# https://www.acmicpc.net/problem/2630
import sys


def devide(row, col, step):
    global count
    flag = table[row][col]

    if step == 1:
        count[flag] += 1
        return

    for i in range(row, row + step):
        for j in range(col, col + step):
            if table[i][j] != flag:
                devide(row, col, step // 2)  # 좌상
                devide(row + step // 2, col, step // 2)  # 좌하
                devide(row, col + step // 2, step // 2)  # 우상
                devide(row + step // 2, col + step // 2, step // 2)  # 우하
                return

    count[flag] += 1


N = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = [0, 0]
devide(0, 0, N)
print(count[0], count[1], sep="\n")
