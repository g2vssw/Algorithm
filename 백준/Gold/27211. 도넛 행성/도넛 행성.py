import sys
from collections import deque

input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(si, sj):
    
    queue =  deque([(si, sj)])
    visited[i][j] = True

    while queue:
        
        ci, cj = queue.popleft()
        
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                if ni < 0:
                    ni = N - 1
                elif ni >= N:
                    ni = 0
                elif nj < 0:
                    nj = M - 1
                else:
                    nj = 0

            if arr[ni][nj] == 1 or visited[ni][nj] == True:
                continue

            visited[ni][nj] = True
            queue.append((ni, nj))

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == False:
            bfs(i, j)
            cnt += 1

print(cnt)