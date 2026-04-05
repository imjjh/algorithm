from collections import deque

def solution(graph, start):
    answer = 0
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    while queue:
        row, col = queue.popleft()
        for dr, dc in control:
            next_r = row + dr
            next_c = col + dc
            # 범위 이내, 방문한적 없으면서, 벽이 아닌 곳
            if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) and not visited[next_r][next_c] and board[next_r][next_c]!="X":
                visited[next_r][next_c] = True
                queue.append((next_r,next_c))
                
                if board[next_r][next_c] == "P":
                    answer +=1 
    
    if answer == 0:
        return "TT"

    return answer


n,m = map(int,(input().split()))

control = [(0,1), (1,0), (-1,0),(0,-1)]

board = []
visited = [[False] * m for i in range(n)]
for i in range(n):
    board.append(input())

# 0-based "I"
for i in range(n):
    if "I" in board[i]:
        row = i
        col = board[i].find("I")
        break
    
print(solution(board,(row,col)))
