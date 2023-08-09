import sys

query = list(sys.stdin.readline().rstrip())
len = len(query)
half_len = len//2
cnt = 0

for idx in range(half_len):
    cnt += (query[idx] == query[len-idx-1])

print(int(cnt == len//2))