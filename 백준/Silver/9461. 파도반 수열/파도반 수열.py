T = int(input())
P = [1, 1, 1]

for i in range(3, 101):
    P.append(P[i - 2] + P[i - 3])

print(*[P[int(input()) - 1] for _ in range(T)], sep="\n")
