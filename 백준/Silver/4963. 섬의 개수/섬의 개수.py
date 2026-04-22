import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    global cnt

    if arr[i][j] == 0:
        return
    elif arr[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = 1
        cnt += 1

    for k in range(8):
        ni, nj = i + di[k], j + dj[k]

        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        elif arr[ni][nj] == 0 or visited[ni][nj] == 1:
            continue
        elif arr[ni][nj] == 1 or visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj)

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1:
                continue
            dfs(i, j)

    print(cnt)