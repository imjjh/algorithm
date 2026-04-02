from collections import Counter
import math

def solution(n):
    curr = n
    num_list = []

    for i in range(2,1000):
        while curr % i == 0:
            curr //= i
            num_list.append(i)

    answer = 1
    for v in Counter(num_list).values():
        answer *= v + 1
            
    return answer
        
