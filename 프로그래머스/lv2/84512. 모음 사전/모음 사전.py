from itertools import product

def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    all = []
    for i in range(5):
        for alph in product(vowels, repeat=i+1):
            all.append(''.join(alph))
    all.sort()
    answer = all.index(word) + 1    
    return answer