from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    int_dict = defaultdict(int)    
    queue = deque([1])
    int_dict[1] = 0
    
    # for 대신 인접리스트를 직접 정의 (양방향)
    graph = [[] for i in range(n+1)]
    for start,end in edge:
        graph[start].append(end)
        graph[end].append(start)
        

    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if next not in int_dict:
                int_dict[next] = int_dict[curr] + 1
                queue.append(next)
    
    length=[]
    
    for key,value in int_dict.items():
        length.append(value)
        print(key,value)
    
    return length.count(max(length))
        
                
        
    
    return answer
    