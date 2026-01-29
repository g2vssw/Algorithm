import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(i, j):
    global submerged

    submerged[i][j] = 1
    queue = deque([(i, j)])

    while queue:

        ci, cj = queue.popleft()

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N or submerged[ni][nj] == 1:
                continue
            submerged[ni][nj] = 1
            queue.append((ni, nj))

max_r = -1
for li in arr:
    max_r = max(max_r, max(li))

max_cnt = 1
for rain in range(1, max_r + 1):
    submerged = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= rain:
                submerged[i][j] = 1
            
    for i in range(N):
        for j in range(N):
            if submerged[i][j]:
                continue
            cnt += 1
            bfs(i, j)
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)