import sys

input = sys.stdin.readline
N, M = map(int, input().split())

words = {}
info = []
idx = 0

for _ in range(N):
    word = input().rstrip()
    ele1 = -1
    ele2 = len(word)
    if ele2 < M:
        continue
    if word not in words.keys():
        words[word] = idx
        idx += 1
        info.append([ele1, -1 * ele2, word])
    else:
        info[words[word]][0] -= 1

res = sorted(info)
for w in res:
    print(w[-1])
