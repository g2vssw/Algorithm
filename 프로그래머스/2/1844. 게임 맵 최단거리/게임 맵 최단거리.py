from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(i, j, visited):
    
    n, m = len(visited), len(visited[0])
    
    queue = deque([(i, j)])
    
    while queue:
        
        ci, cj = queue.popleft()
        
        if ci == n - 1 and cj == m - 1:
            return visited[ci][cj]
        
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 1:
                visited[ni][nj] = visited[ci][cj] + 1
                queue.append((ni, nj))
    return -1
        

def solution(maps):
    
    answer = bfs(0, 0, maps)
    
    return answer