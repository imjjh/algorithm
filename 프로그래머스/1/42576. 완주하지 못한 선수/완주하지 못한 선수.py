from collections import defaultdict

def solution(participant, completion):
    names = defaultdict(int)
    
    for p in participant:
        names[p] += 1
    
    for c in completion:
        names[c] -= 1
    
    for key, value in names.items():
        if value != 0:
            return key
    
