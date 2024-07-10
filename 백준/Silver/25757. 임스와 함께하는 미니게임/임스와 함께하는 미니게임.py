import sys

input = sys.stdin.readline
games = {"Y": 2, "F": 3, "O": 4}
players = set()

n, g = input().split()
n = int(n)
g = games[g] - 1

for i in range(n):
    name = input()
    if name not in players:
        players.add(name)

print(len(players) // g)