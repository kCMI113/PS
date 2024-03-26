import sys

string = sys.stdin.readline().rstrip() + " "  # 편의를 위해 공백 추간
result = ""
tag_flag = 0
word_str = 0
word_end = len(string)

for i in range(len(string)):
    if string[i] == "<":
        tag_flag = 1
        result += string[word_str:i][::-1]
        word_str = i

    if string[i] == ">":
        tag_flag = 0
        result += string[word_str : i + 1]
        word_str = i + 1

    if string[i] == " " and not tag_flag:
        result += string[word_str:i][::-1]
        result += " "
        word_str = i + 1

print(result.rstrip())