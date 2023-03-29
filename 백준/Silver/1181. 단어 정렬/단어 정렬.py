N = int(input())
words = []

for i in range(N):
    w = input()
    if w not in words:
        words.append(w)
    
words.sort(key = lambda x : (len(x),x))

for word in words:
    print(word)