import sys

stu = [0 for _ in range(0,30)]
for _ in range(28):
	i = int(sys.stdin.readline()) -1
	stu[i] = 1

left = 0
right = 29

while(stu[left]):
		left += 1
while(stu[right]):
		right -= 1

print(left+1, right +1)