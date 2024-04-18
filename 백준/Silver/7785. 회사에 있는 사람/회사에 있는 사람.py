import sys

n = int(sys.stdin.readline())
res = {}
name_list = []

for _ in range(n):
	name, state = sys.stdin.readline().split()
	if state == "enter":
		res[name] = 1
	else:
		res[name] = 0
          
for key in res.keys():
	if res[key]:
		name_list.append(key)
  
name_list.sort(reverse=True)
print(*name_list, sep="\n")
          
    