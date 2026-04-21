import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
    queue = deque(start)

    while queue:
        h, i, j = queue.popleft()

        for k in range(6):
            nh, ni, nj = h + dh[k], i + di[k], j + dj[k]

            if nh < 0 or nh >= H or ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            elif arr[nh][ni][nj] == 1 or arr[nh][ni][nj] == -1 or arr[nh][ni][nj] != 0:
                continue
            arr[nh][ni][nj] = arr[h][i][j] + 1
            queue.append((nh, ni, nj))

dh = [0, 0, 0, 0, 1, -1]
di = [-1, 0, 1, 0, 0, 0]
dj = [0, 1, 0, -1, 0, 0]
M, N, H = map(int, input().split())
arr = []
start = deque()
for h in range(H):
    floor = []
    for i in range(N):
        floor.append(list(map(int, input().split())))
    arr.append(floor)


for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                start.append((h, i, j))

bfs(start)

flag = False
result = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0:
                flag = True
            else:
                result = max(arr[h][i][j], result)

if flag:
    print(-1)
else:
    print(result - 1)