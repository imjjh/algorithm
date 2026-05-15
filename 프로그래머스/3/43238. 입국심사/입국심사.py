def solution(n, times):
    start = 0
    end = 1_000_000_000 ** 2
    while start < end:
        mid = (start + end) // 2
        
        people = 0
        for time in times:
            people += mid // time
    
        if n <= people:
            end = mid
        
        elif n > people:
            start = mid + 1
            
    return end
            
            
        
    