def solution(numbers):
    max_1 = 0 
    max_2 = 0
    for num in numbers:
        if max_1 < num:
            max_2 = max_1
            max_1 = num
            
        elif max_2 < num:
            max_2 = num
    answer = max_1 * max_2    
    
    return answer