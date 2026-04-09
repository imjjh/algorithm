from collections import deque

def bfs(graph,start):
    visited = [-1] * len(graph)
    score = 0
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == -1:
                visited[i]= visited[v]+1
                queue.append(i)
                score+=visited[i]

    return score



n, m =map(int,input().split())
graph=[[] for i in range(n+1)]

for i in range(m):

    a,b=map(int,input().split())

    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

scores=[]

for i in range(1,n+1):
    score = bfs(graph,i)
    scores.append((i,score))

scores.sort(key = lambda x: (x[1],x[0]))

print(scores[0][0])