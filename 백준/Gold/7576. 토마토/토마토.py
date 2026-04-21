from collections import deque

def bfs(start):
    queue = deque(start)
    # queue.append(start)

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            elif arr[ni][nj] == 1 or arr[ni][nj] == -1 or arr[ni][nj] != 0:
                continue
            arr[ni][nj] = arr[i][j] + 1
            queue.append((ni, nj))

M, N = map(int, input().split())
arr = []
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

start = deque()
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 1:
            start.append((i, j))

bfs(start)

flag = False
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = True
        else:
            result = max(arr[i][j], result)

if flag:
    print(-1)
else:
    print(result - 1)