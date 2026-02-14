import sys
from collections import deque

input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(si, sj):

    arr[si][sj] = -1
    queue = deque([(si, sj)])

    while queue:

        ci, cj = queue.popleft()

        for k in range(8):
            ni, nj = ci + di[k], cj + dj[k]
            if ni < 0 or ni >= M or nj < 0 or nj >= N or arr[ni][nj] != 1:
                continue
            arr[ni][nj] = -1
            queue.append((ni, nj))

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

result = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(i, j)
            result += 1

print(result)