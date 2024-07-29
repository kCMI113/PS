import sys

input = sys.stdin.readline
string = input().rstrip()
cnt_a = string.count("a")
res = 1000
string += string[:cnt_a]
lidx, ridx = 0, len(string)

while True:
    left_side = string[lidx : lidx + cnt_a]
    right_side = string[ridx - cnt_a : ridx]
    res = min([res, left_side.count("b"), right_side.count("b")])
    if ridx - cnt_a <= lidx:
        break
    lidx += 1
    ridx -= 1

print(res)
