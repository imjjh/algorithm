def solution(n, lost, reserve):
    
    new_reserve= []    
        
    for r in reserve:
        if r in lost:
            lost.remove(r)
        else:
            new_reserve.append(r)
    
            
    reserve = new_reserve
    reserve.sort()
    lost.sort()
    
    
    for r in reserve:
        if 0 < r-1 <= n and r-1 in lost:
            lost.remove(r-1)
        elif 0 < r+1 <= n and r+1 in lost:
            lost.remove(r+1)
            
    return n - len(lost)