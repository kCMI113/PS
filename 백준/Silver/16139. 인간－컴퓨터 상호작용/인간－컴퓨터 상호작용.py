import sys

string = sys.stdin.readline()
n = int(input())
query = [sys.stdin.readline().split() for i in range(n)]
all_alpha = set(list(zip(*query))[0])
cnt = {alpha: [0] for alpha in all_alpha}

for ch in string:
    for alpha in all_alpha:
        if alpha == ch:
            cnt[alpha].append(cnt[alpha][-1]+1)
        else:
            cnt[alpha].append(cnt[alpha][-1])    
  
for ch, start, end in query:
    res = cnt[ch]
    end, start = int(end)+1, int(start)+1
    sys.stdout.write(str(res[end]-res[start-1])+'\n')