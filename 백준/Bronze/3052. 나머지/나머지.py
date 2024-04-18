import sys
res = {}
for _ in range(10):
	num = int(sys.stdin.readline())
	res[num%42] = 1
print(len(res.keys()))