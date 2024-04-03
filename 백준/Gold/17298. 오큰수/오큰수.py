# https://www.acmicpc.net/problem/17298

import sys

N = int(sys.stdin.readline().rstrip())
input_vec = list(map(int, sys.stdin.readline().rstrip().split()))
sub_vec = [input_vec[-1]]
res = [-1]  # 마지막 원소는 언제나 -1

for ele in input_vec[-2::-1]:  # 마지막 원소는 -1이므로 제외하고 반복
    while sub_vec and sub_vec[-1] <= ele:
        # sub_vec = [ele의 오른쪽 원소의 오큰수, ele의 오른쪽 원소]
        # ele보다 작거나 같다면 오큰수가 될 수 없으므로 pop()
        sub_vec.pop()

    if sub_vec:
        # 만약 sub_vec가 비지 않았다면, sub_vec의 마지막이 ele의 오큰수
        res.append(sub_vec[-1])
    else:
        # 만약 sub_vec가 비었다면, ele의 오큰수는 존재하지 않음
        res.append(-1)

    # ele이 ele의 좌측 원소의 오큰수 후보가 되기 때문에 sub_vec에 추가해줌
    sub_vec.append(ele)

print(*res[::-1], sep=" ")
