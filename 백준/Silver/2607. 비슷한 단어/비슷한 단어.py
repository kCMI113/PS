# https://www.acmicpc.net/problem/2607

import sys


def get_construction(word):
    alpha = [0 for _ in range(26)]
    for w in word:
        alpha[ord(w) - ord("A")] += 1
    return alpha


input = sys.stdin.readline
n = int(input())
res = 0
query = input().rstrip()
alpha_q = get_construction(query)

for _ in range(n - 1):
    word = input().rstrip()
    alpha_w = get_construction(word)
    if len(word) == len(query) and sum([abs(alpha_q[i] - alpha_w[i]) for i in range(len(alpha_q))]) <= 2:
        res += 1
    if len(word) != len(query):
        for i in range(ord("A"), ord("Z") + 1):
            temp_q = query + chr(i)
            temp_w = word + chr(i)
            if alpha_q == get_construction(temp_w) or alpha_w == get_construction(temp_q):
                res += 1
                break

print(res)
