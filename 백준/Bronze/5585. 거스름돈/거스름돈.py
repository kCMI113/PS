import sys

pay = 1000
price = int(sys.stdin.readline().rstrip())
remain = pay - price
coins = [500, 100, 50, 10, 5, 1]
res = []

for coin in coins:
    res.append(int(remain / coin))
    remain -= coin * res[-1]
    if remain == 0:
        print(sum(res))
        break