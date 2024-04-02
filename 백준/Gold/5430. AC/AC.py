# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

n_test = int(sys.stdin.readline().rstrip())

for _ in range(n_test):
    is_reverse = False
    is_error = False
    instructions = sys.stdin.readline().rstrip()
    n_num = int(sys.stdin.readline().rstrip())
    vec = sys.stdin.readline().rstrip()[1:-1]

    if vec:
        vec = deque(vec.split(","))

    for inst in instructions:
        if inst == "R":
            is_reverse = not is_reverse
        if inst == "D":
            if not vec:
                is_error = True
                break
            if is_reverse:
                vec.pop()
            if not is_reverse:
                vec.popleft()

    if is_error:
        print("error")
        continue

    print("[", end="")
    if is_reverse:
        print(*[vec.pop() for _ in range(len(vec))], sep=",", end="")
    if not is_reverse:
        print(*[vec.popleft() for _ in range(len(vec))], sep=",", end="")
    print("]")
