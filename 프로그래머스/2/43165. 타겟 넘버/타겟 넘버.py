def solution(numbers, target):
    sums=[numbers[0], -numbers[0]]

    for num in numbers[1:]:
        next_sums = []
        for s in sums:
            next_sums.append(s+num)
            next_sums.append(s-num)
            
            sums = next_sums
    
        
    return sums.count(target)