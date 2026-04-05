from collections import deque

def solution(graph):
    result = [[0] * n for i in range(n)]

    def bfs(i):
        visited = [False] * n
        queue = deque([i])
        
        while queue:
            v = queue.popleft()
            for j in range(n):
                # 이동 가능, 방문한적이 없는 경우
                if graph[v][j] == 1 and  not visited[j]:
                    visited[j]=True
                    queue.append(j)
                    result[i][j]=1

    for i in range(n):
        bfs(i)

    return result

n= int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))


result =  solution(graph)

for row in result:
    print(*row)