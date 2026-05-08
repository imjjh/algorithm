def solution(sizes):
    short=[]
    long=[]
    
    for i in range(len(sizes)):
        short.append(min(sizes[i]))
        long.append(max(sizes[i]))
    
    return max(short) * max(long)