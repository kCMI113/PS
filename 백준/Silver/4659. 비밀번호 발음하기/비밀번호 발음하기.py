import sys

input = sys.stdin.readline
mo = ["a", "e", "i", "o", "u"]
double = ["ee", "oo"]

while True:
    word = input().rstrip()
    flag = 1  # not acc
    jamo = []

    if word == "end":
        break
    for i in range(len(word)):
        if word[i] in mo:
            jamo.append(1)
            flag = 0
        else:
            jamo.append(0)

        if i >= 2 and sum(jamo[i - 2 : i + 1]) in [0, 3]:
            flag = 1
            break

        if i >= 1 and word[i - 1] == word[i] and word[i - 1 : i + 1] not in double:
            flag = 1
            break

    if flag:
        print(f"<{word}> is not acceptable.")
    else:
        print(f"<{word}> is acceptable.")
