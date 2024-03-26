import sys

string = sys.stdin.readline().rstrip()
result = ""
tag_flag = 0
word_str = 0
word_end = len(string)

for i in range(len(string)):
    if string[i] == "<":
        tag_flag = 1
        if i > 0:
            result += string[word_str:i][::-1]

    if tag_flag:
        result += string[i]
        if string[i] == ">":
            tag_flag = 0
            word_str = i + 1
            continue

    if string[i] == " " and not tag_flag:
        result += string[word_str:i][::-1]
        result += " "
        word_str = i + 1

    if i == (len(string) - 1):
        result += string[word_str : i + 1][::-1]

print(result)