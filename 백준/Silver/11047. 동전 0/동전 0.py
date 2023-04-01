
n, price = map(int, input().split())
coins = []
res = 0
for i in range(n):
    coin = int(input())
    if coin > price:
        pass
    else:
        coins.append(coin)

for i in range(-1,-len(coins)-1,-1):
    n_coin = price//coins[i]
    res += n_coin
    price -= n_coin*coins[i]
    
    if not price:
        break
print(res)