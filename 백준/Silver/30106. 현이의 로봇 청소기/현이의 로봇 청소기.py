import sys
from collections import deque

def bfs(i, j):
    global arr

    c = arr[i][j]
    arr[i][j] = 0
    queue = deque([(i, j, c)])
    
    while queue:
        ci, cj, c = queue.popleft()

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] == 0:
                continue
            if c - K <= arr[ni][nj] <= c + K:
                n = arr[ni][nj]
                arr[ni][nj] = 0
                queue.append((ni, nj, n))

input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            continue
        cnt += 1
        bfs(i, j)

print(cnt)