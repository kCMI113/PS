import sys
from collections import Counter

input = sys.stdin.readline
N, M = map(int, input().split())

words = [input().rstrip() for _ in range(N)]
cnter = Counter(word for word in words if len(word) >= M)
words = sorted(list(cnter))
words.sort(key=lambda x: [cnter.get(x), len(x)], reverse=True)
print("\n".join(words))
