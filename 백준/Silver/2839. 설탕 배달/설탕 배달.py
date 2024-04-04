import sys

n = int(sys.stdin.readline())
cnt_t = -1

for i in range(int(n / 5), -1, -1):
    if (n - 5 * i) % 3 == 0:
        cnt_t = (n - 5 * i) // 3
        break

print(cnt_t + i)