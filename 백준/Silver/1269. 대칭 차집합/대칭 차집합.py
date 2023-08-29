import sys

n_a, n_b = sys.stdin.readline().split()
set_a = set(sys.stdin.readline().split())
set_b = set(sys.stdin.readline().split())

diff_ab = set_a.difference(set_b)
diff_ba = set_b.difference(set_a)

print(len(diff_ab) + len(diff_ba))
